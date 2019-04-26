import base64
import requests


def basic_auth():
    base_url = 'https://api.sipgate.com/v2'
    username = 'YOUR_SIPGATE_EMAIL'
    password = 'YOUR_SIPGATE_PASSWORD'

    credentials = (username + ':' + password).encode('utf-8')
    base64_encoded_credentials = base64.b64encode(credentials).decode('utf-8')

    headers = {
        'Authorization': 'Basic ' + base64_encoded_credentials
    }

    response = requests.get(base_url + '/account', headers=headers)

    print('Status:', response.status_code)
    print('Body:', response.content.decode("utf-8"))


if __name__ == "__main__":
    basic_auth()
