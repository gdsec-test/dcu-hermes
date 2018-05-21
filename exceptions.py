class UnsupportedTemplateException(Exception):
    """ An unsupported template was requested """


class UnsupportedNamespaceException(Exception):
    """ An unsupported namespace was requested """


class InvalidSubstitutionValuesError(Exception):
    """ Invalided substitution parameters were provided """
