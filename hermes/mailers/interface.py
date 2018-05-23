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

    @abc.abstractmethod
    def get_status(self, identifier, **kwargs):
        """
        A generic interface for checking on the status of a sent email. Implementors of this interface may choose to
        pass optional and supplementary parameters via kwargs. See each individual concrete implementation for guidance
        on extra parameters.

        :param identifier:
        :param kwargs:
        :return:
        """


class RegisteredMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None, **kwargs):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, recipients=None, **kwargs):
        if recipients:
            email_params['recipients'] = recipients

        return self._client.send_shopper_email(email_params)

    def get_status(self, identifier, **kwargs):
        return self._client.get_status(identifier)


class HostedMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None, **kwargs):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, recipients=None, **kwargs):
        if recipients:
            email_params['recipients'] = recipients

        return self._client.send_shopper_email(email_params)

    def get_status(self, identifier, **kwargs):
        return self._client.get_status(identifier)


class CSAMMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None, **kwargs):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, recipients=None, **kwargs):
        if recipients:
            email_params['recipients'] = recipients

        return self._client.send_shopper_email(email_params)

    def get_status(self, identifier, **kwargs):
        return self._client.get_status(identifier)


class FraudMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None, **kwargs):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, recipients=None, **kwargs):
        if recipients:
            email_params['recipients'] = recipients

        return self._client.send_non_shopper_email(email_params)

    def get_status(self, identifier, **kwargs):
        return self._client.get_status(identifier)


class ForeignMailer(Mailer):
    def __init__(self, env=None, cert=None, key=None, **kwargs):
        self._client = OCMClient(env, (cert, key))

    def send_mail(self, email_params, recipients=None, **kwargs):
        if recipients:
            email_params['recipients'] = recipients

        return self._client.send_non_shopper_email(email_params)

    def get_status(self, identifier, **kwargs):
        return self._client.get_status(identifier)
