"""
Templates.py is responsible for housing all OCM templates. These are templates are organized by type and scoped with
an appropriate namespace to avoid conflicts. e.g. registered.suspend and hosted.suspend.

One must pass the fully qualified template name to send_mail e.g. <namespace>.<template>. Failure to pass in this format
will result in an error.

"""

''' Registered Only Namespace Templates '''
_registered_templates = {
    'suspend_intentionally_malicious': {  # Template ID 4044
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'GDDomainSuspension',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY']
    },
    'suspension_warning': {  # Template ID 3132
        'templateNamespaceKey': 'Hosting',
        'templateTypeKey': 'AbuseRegOnlyCustomer',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'SANITIZED_URL']
    },
    'suspend': {  # Template ID 3760
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'DomainShopperSuspension',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY',
                               'SANITIZED_URL']
    }
}

''' Hosted Namespace Templates '''
_hosted_templates = {
    'suspension_warning': {  # Template ID 3996
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCU24HourWarning',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'MALICIOUS_CONTENT_REPORTED']
    },

    'content_removed': {  # Template ID 3994
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCUContentRemoved',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'MALICIOUS_CONTENT_REMOVED']
    },

    'suspend': {  # Template ID 3998
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCUHostingSuspension',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'MALICIOUS_CONTENT_REPORTED']
    },
    'suspend_intentionally_malicious': {  # Template ID 4046
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'GDHostingSuspension',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY']
    }
}

''' CSAM Namespace Templates '''
_csam_templates = {
    'user_gen_warning': {  # Template ID 4070
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'CSAMViolationNotice',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'LOCATION']
    }
}

''' Fraud Namespace Templates '''
_fraud_templates = {
    'new_shopper_account': {  # Template ID 3693
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCU7days',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'BRAND_TARGETED',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY',
                               'SHOPPER_CREATION_DATE',
                               'SANITIZED_URL']
    },
    'new_domain_registration': {  # Template ID 3716
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCUNewDomainFraud',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'BRAND_TARGETED',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY',
                               'DOMAIN_CREATION_DATE',
                               'SANITIZED_URL']
    },

    'intentionally_malicious_domain': {  # Template ID 3694
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCUSingleClick',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'BRAND_TARGETED',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY',
                               'SANITIZED_URL']
    }
}

''' Foreign Namespace Templates '''
_foreign_templates = {
    'hosting_abuse_notice': {  # Template ID 3103/3104
        'templateNamespaceKey': 'Hosting',
        'templateTypeKey': 'AbuseRegOnlyToHost',
        'substitutionValues': ['DOMAIN',
                               'SANITIZED_URL']
    }
}

namespace_mappings = {
    'fraud': _fraud_templates,
    'csam': _csam_templates,
    'hosted': _hosted_templates,
    'registered': _registered_templates,
    'foreign': _foreign_templates
}

templates = []  # Provides a list of all fully qualified template names <namespace>.<template>
for namespace, mappings in namespace_mappings.iteritems():
    for template_name, _ in mappings.iteritems():
        templates.append(namespace + '.' + template_name)
