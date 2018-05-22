import json

import requests

from hermes.exceptions import UnsupportedEnvironmentException


class OCMClient:
    supported_environments = ['dev', 'prod']

    def __init__(self, env, cert):
        if env not in self.supported_environments:
            raise UnsupportedEnvironmentException("Unsupported environment {}".format(env))

        self._cert = cert

        if env == 'prod':
            self.non_shopper_endpoint = 'https://messaging.api.int.godaddy.com/v1/messaging/messages/sendNonShopper'
            self.shopper_endpoint = 'https://messaging.api.int.godaddy.com/v1/messaging/messages'
        else:
            self.non_shopper_endpoint = 'https://messaging.api.int.dev-godaddy.com/v1/messaging/messages/sendNonShopper'
            self.shopper_endpoint = 'https://messaging.api.int.dev-godaddy.com/v1/messaging/messages'

    def send_shopper_email(self, email_params):
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'X-Shopper-Id': email_params.get('substitutionValues').get('ACCOUNT_NUMBER')}

        response = requests.post(self.shopper_endpoint, headers=headers, json=email_params, cert=self._cert)

        response.raise_for_status()
        return json.loads(response.text)

    def send_non_shopper_email(self, email_params):
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'X-Private-Label-Id': '1'}

        response = requests.post(self.non_shopper_endpoint, headers=headers, json=email_params, cert=self._cert)

        response.raise_for_status()
        return json.loads(response.text)
