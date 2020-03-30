import abc

from hermes.mailers.interface import Mailer
from hermes.connectors.ocm import OCMClient
from hermes.exceptions import UnsupportedValueException


class OCM(Mailer):
    __metaclass__ = abc.ABCMeta

    def __init__(self, env=None, cert=None, key=None, **kwargs):
        """
        :param env: optional runtime env if exists in kwargs
        :param cert: optional certificate path if exists in kwargs
        :param key: optional key path if exists in kwargs
        """
        super(OCM, self).__init__()
        self.env = env
        self._client = OCMClient(env, (cert, key))

    def get_status(self, identifier, **kwargs):
        """
        A generic interface for checking on the status of a sent email. Implementors of this interface may choose to
        pass optional and supplementary parameters via kwargs.

        :param identifier:
        :param kwargs:
        :return:
        """
        return self._client.get_status(identifier)


class RegisteredMailer(OCM):
    def send_mail(self, email_params, domain_id=None, recipients=None, **kwargs):
        """
        ICANN requires domain admin contact be included in warnings/suspension notices sent to customer. email_params
        updated to include new payload details that meet this requirement.
        This method will send to shopper addresses for prod, but if recipients has a
        non-(null/empty) value, then we know the env is non-prod, and should send the non-shopper email
        :param email_params: dict containing substitution values and keys
        :param domain_id: optional 'domain_id' key if exists in kwargs
        :param recipients: optional 'recipients' key if exists in kwargs
        :param kwargs: used indirectly by domain_id and recipients
        """
        try:
            domain_id = int(domain_id)
        except Exception:
            raise UnsupportedValueException("Invalid domainId value provided: {}".format(domain_id))

        if self.env != 'prod' and recipients:
            email_params['recipients'] = recipients
            return self._client.send_non_shopper_email(email_params)

        email_params.update({
            'sendToShopper': True,
            'transformationData': {
                'domainContactLookup': ['Administrative'],
                'domains':  [{'id': domain_id, 'name': email_params.get('substitutionValues').get('DOMAIN')}]
            }
        })
        return self._client.send_shopper_email(email_params)


class HostedMailer(OCM):
    def send_mail(self, email_params, recipients=None, **kwargs):
        """
        This method will send to shopper addresses for prod, but if recipients has a
        non-(null/empty) value, then we know the env is non-prod, and should send the non-shopper email
        :param email_params: dict containing substitution values and keys
        :param recipients: optional 'recipients' key if exists in kwargs
        :param kwargs: used indirectly by recipients
        """
        if self.env != 'prod' and recipients:
            email_params['recipients'] = recipients
            return self._client.send_non_shopper_email(email_params)

        return self._client.send_shopper_email(email_params)


class CSAMMailer(OCM):
    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class ForeignMailer(OCM):
    def send_mail(self, email_params, recipients=None, **kwargs):
        """
        This method will always send to a non-shopper email address.
        :param email_params: dict containing substitution values and keys
        :param recipients: optional 'recipients' key if exists in kwargs
        :param kwargs: used indirectly by recipients
        """
        if self.env != 'prod' and recipients:
            email_params['recipients'] = recipients

        return self._client.send_non_shopper_email(email_params)


class IrisShimMailer(OCM):
    def send_mail(self, email_params, recipients=None, **kwargs):
        """
        This method will always send to a non-shopper email address.
        :param email_params: dict containing substitution values and keys
        :param recipients: optional 'recipients' key if exists in kwargs
        :param kwargs: used indirectly by recipients
        """
        if self.env != 'prod' and recipients:
            email_params['recipients'] = recipients

        return self._client.send_non_shopper_email(email_params)
