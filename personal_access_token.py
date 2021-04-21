import base64
import requests


def personal_access_token():
    base_url = 'https://api.sipgate.com/v2'
    token_id = 'YOUR_SIPGATE_TOKEN_ID'
    token = 'YOUR_SIPGATE_TOKEN'

    credentials = (token_id + ':' + token).encode('utf-8')
    base64_encoded_credentials = base64.b64encode(credentials).decode('utf-8')

    headers = {
        'Authorization': 'Basic ' + base64_encoded_credentials
    }

    response = requests.get(base_url + '/account', headers=headers)

    print('Status:', response.status_code)
    print('Body:', response.content.decode("utf-8"))


if __name__ == "__main__":
    personal_access_token()
