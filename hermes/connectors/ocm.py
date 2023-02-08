import json
from typing import Optional

import requests

from hermes.exceptions import OCMException, UnsupportedEnvironmentException


class OCMClient:
    supported_environments = ['dev', 'test', 'prod']
    success_status = ['PURGED', 'PENDING', 'SUCCESS']  # Everything but 'FAILED'

    def __init__(self, env, cert):
        if env not in self.supported_environments:
            raise UnsupportedEnvironmentException("Unsupported environment {}".format(env))

        self._cert = cert
        self._jwt = None

        if env == 'prod':
            self.non_shopper_endpoint = 'https://messaging.api.int.godaddy.com/v1/messaging/messages/sendNonShopper'
            self.shopper_endpoint = 'https://messaging.api.int.godaddy.com/v1/messaging/messages'
            self._sso_endpoint = 'https://sso.gdcorp.tools/v1/secure/api/token'
        elif env == 'test':
            self.non_shopper_endpoint = 'https://messaging.api.int.test-godaddy.com/v1/messaging/messages/sendNonShopper'
            self.shopper_endpoint = 'https://messaging.api.int.test-godaddy.com/v1/messaging/messages'
            self._sso_endpoint = 'https://sso.test-gdcorp.tools/v1/secure/api/token'
        else:
            self.non_shopper_endpoint = 'https://messaging.api.int.dev-godaddy.com/v1/messaging/messages/sendNonShopper'
            self.shopper_endpoint = 'https://messaging.api.int.dev-godaddy.com/v1/messaging/messages'
            self._sso_endpoint = 'https://sso.dev-gdcorp.tools/v1/secure/api/token'

    def send_shopper_email(self, email_params):
        headers = {'Accept': 'application/json', 'X-Shopper-Id': email_params.get('substitutionValues').get('ACCOUNT_NUMBER')}
        return self._make_request(self.shopper_endpoint, headers, email_params)

    def send_non_shopper_email(self, email_params):
        headers = {'Accept': 'application/json', 'X-Private-Label-Id': '1'}
        return self._make_request(self.non_shopper_endpoint, headers, email_params)

    def get_status(self, message_id):
        assert isinstance(message_id, str)
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        resp_dict = self._make_request(self.shopper_endpoint + '/' + message_id, headers, None)

        if resp_dict.get('status') not in self.success_status:
            raise OCMException(resp_dict.get('failureReason'))
        return resp_dict.get('status')

    def _make_request(self, url: str, headers: dict, body: Optional[dict]) -> dict:
        headers.update({'Authorization': f'sso-jwt {self._get_jwt(False)}'})
        response = requests.post(url, headers=headers, json=body)
        if response.status_code in [401, 403]:
            headers.update({'Authorization': f'sso-jwt {self._get_jwt(True)}'})
        response.raise_for_status()
        return json.loads(response.text)

    def _get_jwt(self, force: bool) -> Optional[str]:
        if not self._jwt or force:
            try:
                response = requests.post(self._sso_endpoint, data={'realm': 'cert'}, cert=self._cert)
                response.raise_for_status()
                return json.loads(response.text).get('data')
            except Exception:
                pass
        return self._jwt
