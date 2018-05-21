import exceptions

from mailers.factory import Factory
from templates import namespace_mappings


def send_mail(template, substitution_values, **kwargs):
    assert isinstance(template, str)
    assert isinstance(substitution_values, dict)

    namespace, t = template.split('.')

    if namespace not in namespace_mappings:
        raise exceptions.UnsupportedNamespaceException("Unsupported namespace {}".format(namespace))

    if t not in namespace_mappings[namespace]:
        raise exceptions.UnsupportedTemplateException("Unsupported template {}".format(t))

    mapping = namespace_mappings[namespace][t]

    expected_values = mapping['substitutionValues']
    if len(expected_values) != len(substitution_values.keys()):
        raise exceptions.InvalidSubstitutionValuesError("Incorrect number of values provided. Expected {} got {}".format(
            len(expected_values), len(substitution_values.keys())))

    for k, v in substitution_values.iteritems():
        if k not in expected_values:
            raise exceptions.InvalidSubstitutionValuesError("Invalid substitution value provided {}".format(k))

    email_params = {'templateNamespaceKey': mapping.get('templateNamespaceKey'),
                    'templateTypeKey': mapping.get('substitutionValues'),
                    'substitutionValues': substitution_values}

    mailer = Factory.get_mailer(namespace)
    return mailer.send_mail(email_params, **kwargs)
