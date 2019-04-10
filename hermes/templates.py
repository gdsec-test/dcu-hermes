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
                               'SANITIZED_URL',
                               'IPADDRESS']
    }
}

''' Iris Shim Templates '''
_iris_shim_templates = {
    'failed_to_parse_report': {  # Template ID 4320/4321
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'ReportAbuse',
        'substitutionValues': []
    },
    'report_successfully_parsed': { # Template ID 4396/4397
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'AbuseReportReceived',
        'substitutionValues': []
    },
    'report_successfully_closed': { # Template ID 4394/4395
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'AbuseReportFinished',
        'substitutionValues': []
    }
}

_smtp_templates = {
    'ssl_revocation': {
        'to': 'practices@godaddy.com',
        'from': 'dcuinternal@godaddy.com',
        'subject': 'SSL revocation request',
        'email_body': '''Hello,\n\nThe Digital Crimes Unit is requesting the revocation of an SSL due to Terms of Service violations.
        \nShopper Number: {SHOPPER}\n\nCertificate Details:\n{CERT_DETAILS}\nRegards,\nDigital Crimes Unit\nGoDaddy''',
        'substitutionValues': ['CERT_DETAILS', 'SHOPPER']
    }
}

namespace_mappings = {
    'fraud': _fraud_templates,
    'csam': _csam_templates,
    'hosted': _hosted_templates,
    'registered': _registered_templates,
    'foreign': _foreign_templates,
    'iris_shim': _iris_shim_templates,
    'smtp': _smtp_templates
}

templates = []  # Provides a list of all fully qualified template names <namespace>.<template>
for namespace, mappings in namespace_mappings.iteritems():
    for template_name, _ in mappings.iteritems():
        templates.append(namespace + '.' + template_name)
