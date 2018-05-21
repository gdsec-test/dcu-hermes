import requests


class OCMClient:

    def __init__(self, env, cert):
        self._cert = cert

        if env == 'prod':
            self.non_shopper_endpoint = 'https://messaging.api.int.godaddy.com/v1/messaging/messages/sendNonShopper'
            self.shopper_endpoint = 'https://messaging.api.int.godaddy.com/v1/messaging/messages'
        else:
            self.non_shopper_endpoint = 'https://messaging.api.int.dev-godaddy.com/v1/messaging/messages/sendNonShopper'
            self.shopper_endpoint = 'https://messaging.api.int.dev-godaddy.com/v1/messaging/messages'

    def send_shopper_email(self, params):
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'X-Shopper-Id': params.get('substitutionValues').get('ACCOUNT_NUMBER')}

        response = requests.post(self.shopper_endpoint, headers=headers, json=params, cert=self._cert)

        response.raise_for_status()
        return response.json()

    def send_non_shopper_email(self, params):
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json',
                   'X-Private-Label-Id': '1'}

        response = requests.post(self.non_shopper_endpoint, headers=headers, json=params, cert=self._cert)

        response.raise_for_status()
        return response.json()
