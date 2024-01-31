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
    'suspend_shopper_compromise': {  # Template ID 6480
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'CustomersSecurityIncident',
        'substitutionValues': ['ACCOUNT_NUMBER']
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
    },
    'forwarding_complaint': {  # Template ID 5518
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'ForwardedComplaintNotice',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'SANITIZED_URL']
    },
    'repeat_offender': {  # Template ID 5493
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'Registered_Repeat_Offender_Domains',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'SANITIZED_URL']
    },
    'sucuri_warning': {  # Template ID 6041
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'DCUSucuriCustomerWarning',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
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
    'suspend_shopper_compromise': {  # Template ID 6480
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'CustomersSecurityIncident',
        'substitutionValues': ['ACCOUNT_NUMBER']
    },
    'extensive_compromise': {  # Template ID 4809
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'DCUExtensiveCompromise',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN']
    },
    'sucuri_warning': {  # Template ID 6041
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'DCUSucuriCustomerWarning',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN',
                               'SANITIZED_URL']
    },
    'suspend_pci_compliance': {  # Template ID 6471
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'PCIComplianceSuspension',
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
    },
    'suspend': {  # Template ID 5722
        'templateNamespaceKey': 'Abuse',
        'templateTypeKey': 'ChildAbuseInvestigation ',
        'substitutionValues': ['ACCOUNT_NUMBER',
                               'DOMAIN']
    }
}

''' Foreign Namespace Templates '''
_foreign_templates = {
    'hosting_abuse_notice': {  # Template ID 3103
        'templateNamespaceKey': 'Hosting',
        'templateTypeKey': 'AbuseRegOnlyToHost',
        'substitutionValues': ['DOMAIN',
                               'SANITIZED_URL',
                               'IPADDRESS']
    }
}

''' Reporter Namespace Templates '''
_reporter_templates = {
    'mail_reporter': {  # Template ID 7010
        'templateNamespaceKey': 'Iris',
        'templateTypeKey': 'AbuseReportConfirmation',
        'substitutionValues': {}
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
        'subject': 'Malicious activity on a newly created account: {ACCOUNT_NUMBER}',
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
        'subject': 'Suspected malicious activity: {ACCOUNT_NUMBER}',
        'email_body': '''Dear Fraud,
        \n\nPlease check account {ACCOUNT_NUMBER} which owns domain {DOMAIN} created on {DOMAIN_CREATION_DATE} for possible Fraud or shopper compromise.
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
        'subject': 'Suspected intentionally malicious activity: {ACCOUNT_NUMBER}',
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
    },
    'compromised_shopper_account': {
        'to': fraud_email,
        'from': dcuinternal_email,
        'subject': 'Suspected compromised shopper account: {ACCOUNT_NUMBER}',
        'email_body': '''Dear Fraud,
        \n\nPlease check account {ACCOUNT_NUMBER} for possible Fraud as the account may have been compromised.
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
    'ssl': _ssl_templates,
    'reporter': _reporter_templates
}

templates = []  # Provides a list of all fully qualified template names <namespace>.<template>
for namespace, mappings in list(namespace_mappings.items()):
    for template_name, _ in list(mappings.items()):
        templates.append(namespace + '.' + template_name)
