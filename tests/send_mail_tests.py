from json import dumps

from mock import patch, MagicMock
from nose.tools import assert_raises, assert_equal

from hermes.exceptions import UnsupportedTemplateException, \
    UnsupportedNamespaceException, \
    InvalidSubstitutionValuesException, \
    UnsupportedEnvironmentException
from hermes.messenger import send_mail


class TestSendMail:
    """ Tests basic functionality of driver and proper delegation of namespaces/templates """

    ''' Driver Tests '''
    def test_invalid_namespace(self):
        assert_raises(UnsupportedNamespaceException, send_mail, 'netvio.customer_warning', {})

    def test_invalid_template(self):
        assert_raises(UnsupportedTemplateException, send_mail, 'fraud.suspend', {})

    def test_bad_substitution_length(self):
        substitution_values = {'DOMAIN': 'test-domain', 'SANITIZED_URL': 'hxxp://godaddy.com', 'extra': 'parameter'}
        assert_raises(InvalidSubstitutionValuesException,
                      send_mail, 'foreign.hosting_abuse_notice', substitution_values)

    def test_bad_missing_substitution_values(self):
        substitution_values = {'DOMAIN': 'test-domain', 'extra': 'parameter'}
        assert_raises(InvalidSubstitutionValuesException,
                      send_mail, 'foreign.hosting_abuse_notice', substitution_values)

    ''' Tests creation of each specific mailer '''
    def test_send_unsupported_environment(self):
        substitution_values = {'DOMAIN': 'test-domain', 'SANITIZED_URL': 'hxxp://godaddy.com'}
        assert_raises(UnsupportedEnvironmentException,
                      send_mail, 'foreign.hosting_abuse_notice', substitution_values)

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps({'request_id': 'test-id'})))
    def test_send_foreign(self, mock_post):
        substitution_values = {'DOMAIN': 'test-domain', 'SANITIZED_URL': 'hxxp://godaddy.com'}
        actual = send_mail('foreign.hosting_abuse_notice', substitution_values, **{'recipients': 'no-reply@godaddy.com',
                                                                                   'env': 'dev'})
        assert_equal({'request_id': 'test-id'}, actual)

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps({'request_id': 'test-id'})))
    def test_send_hosted(self, mock_post):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://godaddy.com', 'MALICIOUS_CONTENT_REPORTED': ''}
        actual = send_mail('hosted.suspension_warning', substitution_values, **{'env': 'dev'})
        assert_equal({'request_id': 'test-id'}, actual)

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps({'request_id': 'test-id'})))
    def test_send_registered(self, mock_post):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://godaddy.com', 'MALICIOUS_ACTIVITY': ''}
        actual = send_mail('registered.suspend_intentionally_malicious', substitution_values, **{'env': 'dev'})
        assert_equal({'request_id': 'test-id'}, actual)

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps({'request_id': 'test-id'})))
    def test_send_csam(self, mock_post):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://godaddy.com', 'LOCATION': ''}
        actual = send_mail('csam.user_gen_warning', substitution_values, **{'env': 'dev'})
        assert_equal({'request_id': 'test-id'}, actual)

    @patch('requests.post', return_value=MagicMock(status_code=201, text=dumps({'request_id': 'test-id'})))
    def test_send_fraud(self, mock_post):
        substitution_values = {'ACCOUNT_NUMBER': 'test-id', 'DOMAIN': 'hxxp://godaddy.com', 'BRAND_TARGETED': '',
                               'MALICIOUS_ACTIVITY': '', 'SHOPPER_CREATION_DATE': '', 'SANITIZED_URL': ''}
        actual = send_mail('fraud.new_shopper_account', substitution_values, **{'env': 'dev'})
        assert_equal({'request_id': 'test-id'}, actual)
