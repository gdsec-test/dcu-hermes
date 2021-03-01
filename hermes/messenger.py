import copy

from hermes.exceptions import UnsupportedNamespaceException, \
    InvalidSubstitutionValuesException, \
    UnsupportedTemplateException

from hermes.mailers.factory import MailerFactory
from .templates import namespace_mappings


def send_mail(template, substitution_values, **kwargs):
    assert isinstance(template, str)
    assert isinstance(substitution_values, dict)

    namespace, t = template.split('.')

    if namespace not in namespace_mappings:
        raise UnsupportedNamespaceException("Unsupported namespace {}".format(namespace))

    if t not in namespace_mappings[namespace]:
        raise UnsupportedTemplateException("Unsupported template {}".format(t))

    mapping = namespace_mappings[namespace][t]

    expected_values = mapping['substitutionValues']
    if len(expected_values) != len(list(substitution_values.keys())):
        raise InvalidSubstitutionValuesException("Incorrect number of values provided. Expected {} got {}".format(
            len(expected_values), len(list(substitution_values.keys()))))

    for k, v in list(substitution_values.items()):
        if k not in expected_values:
            raise InvalidSubstitutionValuesException("Invalid substitution value provided {}".format(k))

    if namespace in MailerFactory.smtp_templates:
        # For all SMTP/XARF related emails
        email_body = mapping.get('email_body', '')
        subject = mapping.get('subject', '')
        email_params = copy.deepcopy(mapping)
        email_params.update({'email_body': email_body.format(**substitution_values),
                             'subject': subject.format(**substitution_values)})
    else:
        # For all emails that need to be sent via OCM
        email_params = {'templateNamespaceKey': mapping.get('templateNamespaceKey'),
                        'templateTypeKey': mapping.get('templateTypeKey'),
                        'substitutionValues': substitution_values}

    mailer = MailerFactory.get_mailer(namespace, **kwargs)
    return mailer.send_mail(email_params, **kwargs)


def get_status(template, identifier, **kwargs):
    namespace, t = template.split('.')

    if namespace not in namespace_mappings:
        raise UnsupportedNamespaceException("Unsupported namespace {}".format(namespace))

    if t not in namespace_mappings[namespace]:
        raise UnsupportedTemplateException("Unsupported template {}".format(t))

    mailer = MailerFactory.get_mailer(namespace, **kwargs)
    return mailer.get_status(identifier, **kwargs)
