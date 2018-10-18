class UnsupportedTemplateException(Exception):
    """ An unsupported template was requested """


class UnsupportedNamespaceException(Exception):
    """ An unsupported namespace was requested """


class InvalidSubstitutionValuesException(Exception):
    """ Invalid substitution parameters were provided """


class UnsupportedEnvironmentException(Exception):
    """ A request for an email in an unsupported environment """


class OCMException(Exception):
    """ Any error that may be returned via the OCM system """


class UnsupportedValueException(Exception):
    """ An unsupported value was provided """
