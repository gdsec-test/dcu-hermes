import abc
import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPRecipientsRefused

from hermes.exceptions import InvalidEmailRecipientException, SMTPException


class Mailer(metaclass=abc.ABCMeta):
    def __init__(self, **kwargs):
        self._client = None

    @abc.abstractmethod
    def send_mail(self, email_params, **kwargs):
        """
        A generic interface for sending mail with some email_params. Implementers of this interface may chooses to pass
        optional and supplementary parameters via kwargs such as intended recipients, etc. See each individual concrete
        implementation for guidance on extra parameters.

        :param email_params:
        :param kwargs:
        :return:
        """


class SMTP(Mailer):
    mail_relay = 'relay-app.secureserver.net'
    SUCCESS_MSG = 'SUCCESS'

    def __init__(self, env=None, **kwargs):
        self.env = env

    def send_mail(self, email_params, recipients=None, **kwargs):
        """
        Connect to the mail relay server and send the email.
        :param email_params: The basic parameters required to send an email
        :param recipients: The recipients of the email
        :return:
        """
        server = None

        if self.env != 'prod':
            mail_to = recipients if recipients else []
        else:
            mail_to = email_params.get('to')

        try:
            email_object = MIMEText(email_params.get('email_body'))
            email_object['Subject'] = email_params.get('subject')
            email_object['From'] = email_params.get('from')
            email_object['To'] = ';'.join(mail_to) if isinstance(mail_to, list) else mail_to

            server = smtplib.SMTP(self.mail_relay)
            server.sendmail(email_params.get('from'), mail_to, email_object.as_string())
            return self.SUCCESS_MSG
        except SMTPRecipientsRefused as e:
            raise InvalidEmailRecipientException('The email recipient {} is invalid. More details: {}'.format(mail_to, e.args))
        except Exception as e:
            raise SMTPException('Error while sending the email. More details : {}'.format(e.args))
        finally:
            if server:
                server.quit()
