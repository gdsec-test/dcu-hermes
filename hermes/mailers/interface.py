import abc

from hermes.connectors.ocm import OCMClient


class Mailer:
    __metaclass__ = abc.ABCMeta

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

class RegisteredMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class HostedMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class CSAMMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class FraudMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None, **kwargs):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, recipients=None, **kwargs):
        if not recipients:
            recipients = []

        email_params['recipients'] = recipients
        return self._client.send_non_shopper_email(email_params)


class ForeignMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None, **kwargs):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, recipients=None, **kwargs):
        if not recipients:
            recipients = []

        email_params['recipients'] = recipients
        return self._client.send_non_shopper_email(email_params)

