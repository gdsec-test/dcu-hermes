from json import dumps
from unittest import TestCase
from unittest.mock import MagicMock, patch

from hermes.exceptions import (InvalidEmailRecipientException,
                               InvalidSubstitutionValuesException,
                               UnsupportedEnvironmentException,
                               UnsupportedNamespaceException,
                               UnsupportedTemplateException)
from hermes.messenger import send_mail

id_dict = {'request_id': 'test-id'}


class TestSendMail(TestCase):
    """ Tests basic functionality of driver and proper delegation of namespaces/templates """
    ''' Driver Tests '''
    def test_invalid_namespace(self):
        self.assertRaises(UnsupportedNamespaceException, send_mail, 'netvio.customer_warning', {})

    def test_invalid_template(self):
        self.assertRaises(UnsupportedTemplateException, send_mail, 'fraud.suspend', {})

    def test_bad_substitution_length(self):
        substitution_values = {'DOMAIN': 'test-domain', 'SANITIZED_URL': 'hxxp://godaddy.com', 'extra': 'parameter'}
        self.assertRaises(InvalidSubstitutionValuesException,
                          send_mail, 'foreign.hosting_abuse_notice', substitution_values)

    def test_bad_missing_substitution_values(self):
        substitution_values = {'DOMAIN': 'test-domain', 'extra': 'parameter'}
        self.assertRaises(InvalidSubstitutionValuesException,
                          send_mail, 'foreign.hosting_abuse_notice', substitution_values)

    ''' Tests creation of each specific mailer '''
    def test_send_unsupported_environment(self):
        substitution_values = {'DOMAIN': 'test-domain', 'SANITIZED_URL': 'hxxp://godaddy.com', 'IPADDRESS': 'test-ip'}
        self.assertRaises(UnsupportedEnvironmentException,
                          send_mail, 'foreign.hosting_abuse_notice', substitution_values)

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_foreign(self, mock_post):
        substitution_values = {'DOMAIN': 'test-domain', 'SANITIZED_URL': 'hxxp://godaddy.com', 'IPADDRESS': 'test-ip'}
        actual = send_mail('foreign.hosting_abuse_notice', substitution_values, **{'recipients': 'no-reply_email', 'env': 'dev'})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_hosted(self, mock_post):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://godaddy.com', 'MALICIOUS_CONTENT_REPORTED': ''}
        actual = send_mail('hosted.suspension_warning', substitution_values, **{'env': 'dev'})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_registered(self, mock_post):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://godaddy.com', 'MALICIOUS_ACTIVITY': ''}
        actual = send_mail('registered.suspend_intentionally_malicious', substitution_values, **{'env': 'dev', 'domain_id': 1})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_csam(self, mock_post):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://godaddy.com', 'LOCATION': ''}
        actual = send_mail('csam.user_gen_warning', substitution_values, **{'env': 'dev'})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_csam_suspend(self, mock_post):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://godaddy.com'}
        actual = send_mail('csam.suspend', substitution_values, **{'env': 'dev'})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('hermes.mailers.interface.SMTP.send_mail', return_value='SUCCESS')
    def test_send_fraud_new_shopper(self, mock_sendmail):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://goodaddy.com',
                               'BRAND_TARGETED': 'godaddy.com', 'MALICIOUS_ACTIVITY': 'Phishing',
                               'SHOPPER_CREATION_DATE': '2010-10-27', 'URL': 'hxxp://goodaddy.com/phish'}
        actual = send_mail('fraud.new_shopper_account', substitution_values,
                           **{'env': 'dev', 'recipients': 'dcuinternal@godaddy.com'})
        self.assertEqual(actual, 'SUCCESS')
        mock_sendmail.assert_called()

    @patch('hermes.mailers.interface.SMTP.send_mail', return_value='SUCCESS')
    def test_send_fraud_new_domain(self, mock_sendmail):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://goodaddy.com',
                               'BRAND_TARGETED': 'godaddy.com', 'MALICIOUS_ACTIVITY': 'Phishing',
                               'DOMAIN_CREATION_DATE': '2010-10-27', 'URL': 'hxxp://goodaddy.com/phish'}
        actual = send_mail('fraud.new_domain_registration', substitution_values,
                           **{'env': 'dev', 'recipients': 'dcuinternal@godaddy.com'})
        self.assertEqual(actual, 'SUCCESS')
        mock_sendmail.assert_called()

    @patch('hermes.mailers.interface.SMTP.send_mail', return_value='SUCCESS')
    def test_send_fraud_intentionally_malicious(self, mock_sendmail):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://goodaddy.com',
                               'BRAND_TARGETED': 'godaddy.com', 'MALICIOUS_ACTIVITY': 'Phishing',
                               'URL': 'hxxp://goodaddy.com/phish'}
        actual = send_mail('fraud.intentionally_malicious_domain', substitution_values,
                           **{'env': 'dev', 'recipients': 'dcuinternal@godaddy.com'})
        self.assertEqual(actual, 'SUCCESS')
        mock_sendmail.assert_called()

    @patch('hermes.mailers.interface.SMTP.send_mail', return_value='SUCCESS')
    def test_send_compromised_shopper_account(self, mock_sendmail):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://goodaddy.com',
                               'BRAND_TARGETED': 'godaddy.com', 'MALICIOUS_ACTIVITY': 'Phishing',
                               'URL': 'hxxp://goodaddy.com/phish'}
        actual = send_mail('fraud.compromised_shopper_account', substitution_values,
                           **{'env': 'dev', 'recipients': 'dcuinternal@godaddy.com'})
        self.assertEqual(actual, 'SUCCESS')
        mock_sendmail.assert_called()

    @patch('hermes.mailers.interface.SMTP.send_mail', return_value='SUCCESS')
    def test_send_smtp_success(self, mock_sendmail):
        substitution_values = {'CERT_DETAILS': '''Common Name: *.abc.com \tCreated Date: 2010-10-27\tExpiration Date: 2019-10-28\n''',
                               'SHOPPER': '1234'}
        actual = send_mail('ssl.revocation', substitution_values, **{'recipients': 'kmurthy_email', 'env': 'dev'})
        self.assertEqual(actual, 'SUCCESS')
        mock_sendmail.assert_called()

    @patch('hermes.mailers.interface.SMTP.send_mail', side_effect=InvalidEmailRecipientException())
    def test_send_smtp_invalid_recipient(self, mockSendMail):
        substitution_values = {'CERT_DETAILS': '''Common Name: *.abc.com \tCreated Date: 2010-10-27\tExpiration Date: 2019-10-28\n''', 'SHOPPER': '1234'}
        self.assertRaises(InvalidEmailRecipientException, send_mail, 'ssl.revocation', substitution_values, **{'env': 'dev'})

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_extensive_compromise(self, mock_post):
        substitution_values = {'DOMAIN': 'test-ext-compromise', 'ACCOUNT_NUMBER': 'test-id'}
        actual = send_mail('hosted.extensive_compromise', substitution_values, **{'env': 'dev'})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_reporter_email(self, mock_post):
        substitution_values = {}
        kw_args = {'env': 'dev', 'recipients': 'non-shopper-email-address'}
        actual = send_mail('reporter.mail_reporter', substitution_values, **kw_args)
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_registered_repeat_offender(self, mock_post):
        substitution_values = {'DOMAIN': 'reg-repeat-offender', 'ACCOUNT_NUMBER': 'test-id',
                               'SANITIZED_URL': 'hxxp://reg-repeat-offender'}
        actual = send_mail('registered.repeat_offender', substitution_values, **{'env': 'dev', 'domain_id': 1})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_registered_sucuri_warning(self, mock_post):
        substitution_values = {'DOMAIN': 'reg-sucuri-warning', 'ACCOUNT_NUMBER': 'test-id',
                               'SANITIZED_URL': 'hxxp://reg-sucuri-warning'}
        actual = send_mail('registered.sucuri_warning', substitution_values, **{'env': 'dev', 'domain_id': 1})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_hosted_sucuri_warning(self, mock_post):
        substitution_values = {'DOMAIN': 'hosted-sucuri-warning', 'ACCOUNT_NUMBER': 'test-id',
                               'SANITIZED_URL': 'hxxp://hosted-sucuri-warning'}
        actual = send_mail('hosted.sucuri_warning', substitution_values, **{'env': 'dev', 'domain_id': 1})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps(id_dict)))
    def test_send_suspend_pci_compliance(self, mock_post):
        substitution_values = {'DOMAIN': 'hosted-pci-suspend', 'ACCOUNT_NUMBER': 'test-id'}
        actual = send_mail('hosted.suspend_pci_compliance', substitution_values, **{'env': 'dev', 'domain_id': 1})
        self.assertEqual(id_dict, actual)
        mock_post.assert_called()
