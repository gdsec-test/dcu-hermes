import abc

from hermes.mailers.interface import Mailer
from hermes.connectors.ocm import OCMClient
from hermes.exceptions import UnsupportedValueException


class OCM(Mailer):
    __metaclass__ = abc.ABCMeta

    def __init__(self, env=None, cert=None, key=None, **kwargs):
        super(OCM, self).__init__()
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
    def send_mail(self, email_params, domain_id=None, **kwargs):
        """
        ICANN requires domain admin contact be included in warnings/suspension notices sent to customer. email_params
        updated to include new payload details that meet this requirement.
        """
        try:
            domain_id = int(domain_id)
        except Exception:
            raise UnsupportedValueException("Invalid domainId value provided: {}".format(domain_id))
        email_params.update({
            'sendToShopper': True,
            'transformationData': {
                'domainContactLookup': ['Administrative'],
                'domains':  [{'id': domain_id, 'name': email_params.get('substitutionValues').get('DOMAIN')}]
            }
        })

        return self._client.send_shopper_email(email_params)


class HostedMailer(OCM):
    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class CSAMMailer(OCM):
    def send_mail(self, email_params, **kwargs):
        return self._client.send_shopper_email(email_params)


class FraudMailer(OCM):
    def send_mail(self, email_params, recipients=None, **kwargs):
        if recipients:
            email_params['recipients'] = recipients

        return self._client.send_non_shopper_email(email_params)


class ForeignMailer(OCM):
    def send_mail(self, email_params, recipients=None, **kwargs):
        if recipients:
            email_params['recipients'] = recipients

        return self._client.send_non_shopper_email(email_params)


class IrisShimMailer(OCM):
    def send_mail(self, email_params, recipients=None, **kwargs):
        if recipients:
            email_params['recipients'] = recipients

        return self._client.send_non_shopper_email(email_params)