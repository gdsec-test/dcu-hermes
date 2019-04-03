from hermes.mailers.ocm_interface import RegisteredMailer, \
    HostedMailer, \
    CSAMMailer, \
    FraudMailer, \
    ForeignMailer, \
    IrisShimMailer
from hermes.mailers.interface import SMTP


class MailerFactory:
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
        elif mailer_type == 'iris_shim':
            return IrisShimMailer(**kwargs)
        elif mailer_type == 'smtp':
            return SMTP(**kwargs)
