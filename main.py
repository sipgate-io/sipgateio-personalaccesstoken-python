import base64
import requests


def main():
    baseURL = 'https://api.sipgate.com/v2'
    username = 'YOUR_SIPGATE_EMAIL'
    password = 'YOUR_SIPGATE_PASSWORD'

    credentials = f'{username}:{password}'.encode('utf-8')
    base64EncodedCredentials = base64.b64encode(credentials).decode('utf-8')

    headers = {
        'Authorization': f'Basic {base64EncodedCredentials}'
    }

    response = requests.get(f'{baseURL}/account', headers=headers)

    print(f'Status: {response.status_code}')
    print(f'Body: {response.content.decode("utf-8")}')


if __name__ == "__main__":
    main()
