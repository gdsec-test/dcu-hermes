from connectors.ocm import OCMClient


class Factory:

    @staticmethod
    def get_mailer(mailer_type, **kwargs):
        if mailer_type == 'registered':
            return RegisteredMailer(**kwargs)
        elif mailer_type == 'hosted':
            return HostedMailer(**kwargs)
        elif mailer_type == 'csam':
            return CSAMMailer(**kwargs)
        elif mailer_type == 'fraud':
            return FraudMailer(**kwargs)
        elif mailer_type == 'foreign':
            return ForeignMailer(**kwargs)


class RegisteredMailer:
    def __init__(self, **kwargs):
        self._cert = (kwargs.get('cert'), kwargs.get('key'))
        self._env = kwargs.get('env')
        self._client = OCMClient(self._env, self._cert)

    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class HostedMailer:
    def __init__(self, **kwargs):
        self._cert = (kwargs.get('cert'), kwargs.get('key'))
        self._env = kwargs.get('env')
        self._client = OCMClient(self._env, self._cert)

    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class CSAMMailer:
    def __init__(self, **kwargs):
        self._cert = (kwargs.get('cert'), kwargs.get('key'))
        self._env = kwargs.get('env')
        self._client = OCMClient(self._env, self._cert)

    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class FraudMailer:
    def __init__(self, **kwargs):
        self._cert = (kwargs.get('cert'), kwargs.get('key'))
        self._env = kwargs.get('env')
        self._client = OCMClient(self._env, self._cert)

    def send_mail(self, email_params, **kwargs):
        email_params['recipients'] = kwargs.get('recipients')
        return self._client.send_non_shopper_email(email_params)


class ForeignMailer:
    def __init__(self, **kwargs):
        self._cert = (kwargs.get('cert'), kwargs.get('key'))
        self._env = kwargs.get('env')
        self._client = OCMClient(self._env, self._cert)

    def send_mail(self, email_params, **kwargs):
        email_params['recipients'] = kwargs.get('recipients')
        return self._client.send_non_shopper_email(email_params)

