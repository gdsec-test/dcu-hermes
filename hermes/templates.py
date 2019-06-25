"""
Templates.py is responsible for housing all OCM templates. These are templates are organized by type and scoped with
an appropriate namespace to avoid conflicts. e.g. registered.suspend and hosted.suspend.

One must pass the fully qualified template name to send_mail e.g. <namespace>.<template>. Failure to pass in this format
will result in an error.

"""

''' OCM TEMPLATES '''

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
                               'DOMAIN']
    },
    'repeat_offender': {  # Template ID 4807
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCURepeatOffender',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'SANITIZED_URL']
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
    },
    'extensive_compromise': {  # Template ID 4809
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCUExtensiveCompromise',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN']
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

''' SMTP TEMPLATES '''

fraud_email = 'ccinquiries@godaddy.com'
ssl_email = 'practices@godaddy.com'
dcuinternal_email = 'dcuinternal@godaddy.com'

''' Fraud Namespace Templates '''
_fraud_templates = {
    'new_shopper_account': {
        'to': fraud_email,
        'from': dcuinternal_email,
        'subject': 'Malicious activity on a newly created account.',
        'email_body': '''Dear Fraud,
        \n\nPlease check account {ACCOUNT_NUMBER} created on {SHOPPER_CREATION_DATE} for possible Fraud.
        \n{DOMAIN} is being used for {MALICIOUS_ACTIVITY} targeting {BRAND_TARGETED}.
        \nThe malicious URL is {URL}.
        \n\nRegards,\nDigital Crimes Unit - Engineers''',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'BRAND_TARGETED',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY',
                               'SHOPPER_CREATION_DATE',
                               'URL']
    },
    'new_domain_registration': {
        'to': fraud_email,
        'from': dcuinternal_email,
        'subject': 'Suspected malicious activity.',
        'email_body': '''Dear Fraud,
        \n\nPlease check account {ACCOUNT_NUMBER} which owns domain {DOMAIN} created on {DOMAIN_CREATION_DATE} for possible Fraud.
        \n{DOMAIN} is being used for {MALICIOUS_ACTIVITY} targeting {BRAND_TARGETED}.
        \nThe malicious URL is {URL}.
        \n\nRegards,\nDigital Crimes Unit - Engineers''',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'BRAND_TARGETED',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY',
                               'DOMAIN_CREATION_DATE',
                               'URL']
    },
    'intentionally_malicious_domain': {
        'to': fraud_email,
        'from': dcuinternal_email,
        'subject': 'Suspected intentionally malicious activity',
        'email_body': '''Dear Fraud,
        \n\nPlease check account {ACCOUNT_NUMBER} for possible Fraud.
        \n{DOMAIN} appears to be intentionally used for {MALICIOUS_ACTIVITY} targeting {BRAND_TARGETED}.
        \nThe malicious URL is {URL}.
        \n\nRegards,\nDigital Crimes Unit - Engineers''',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'BRAND_TARGETED',
                               'DOMAIN',
                               'MALICIOUS_ACTIVITY',
                               'URL']
    }
}

''' SSL Templates '''
_ssl_templates = {
    'revocation': {
        'to': ssl_email,
        'from': dcuinternal_email,
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
    'ssl': _ssl_templates
}

templates = []  # Provides a list of all fully qualified template names <namespace>.<template>
for namespace, mappings in namespace_mappings.iteritems():
    for template_name, _ in mappings.iteritems():
        templates.append(namespace + '.' + template_name)
