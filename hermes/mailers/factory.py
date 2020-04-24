from hermes.mailers.ocm_interface import RegisteredMailer, \
    HostedMailer, \
    CSAMMailer, \
    ForeignMailer, \
    IrisShimMailer, \
    ReporterMailer
from hermes.mailers.interface import SMTP


class MailerFactory:
    smtp_templates = {'ssl', 'fraud'}

    @staticmethod
    def get_mailer(mailer_type, **kwargs):
        if mailer_type == 'registered':
            return RegisteredMailer(**kwargs)
        elif mailer_type == 'hosted':
            return HostedMailer(**kwargs)
        elif mailer_type == 'csam':
            return CSAMMailer(**kwargs)
        elif mailer_type == 'foreign':
            return ForeignMailer(**kwargs)
        elif mailer_type == 'iris_shim':
            return IrisShimMailer(**kwargs)
        elif mailer_type == 'reporter':
            return ReporterMailer(**kwargs)
        elif mailer_type in MailerFactory.smtp_templates:
            return SMTP(**kwargs)
