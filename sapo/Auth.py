import base64
import hmac
from hashlib import sha256


class Auth:
    @classmethod
    def build_signature(cls, secret, params):
        data_to_sign = sorted(params.items())
        data_to_sign = [f"{k}={v}" for k, v in data_to_sign if v]
        data_string = "&".join(data_to_sign)
        signature = hmac.new(secret.encode(), data_string.encode(), sha256).digest()
        return base64.b64encode(signature).decode("utf-8")

    @classmethod
    def get_access_token(cls, api, code, client_id, client_secret):
        params = {
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
        }
        return api.without_token().post("admin/oauth/access_token", params=params)
