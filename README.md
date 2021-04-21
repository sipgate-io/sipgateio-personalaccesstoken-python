<img src="https://www.sipgatedesign.com/wp-content/uploads/wort-bildmarke_positiv_2x.jpg" alt="sipgate logo" title="sipgate" align="right" height="112" width="200"/>

# sipgate.io python Personal Access Token example

To demonstrate how to authenticate against the sipgate REST API using HTTP Basic Auth, we query the `/account` endpoint which provides basic account information.

For further information regarding the sipgate REST API please visit https://api.sipgate.com/v2/doc.

For more information on how to create a token, visit https://www.sipgate.io/rest-api/authentication#personalAccessToken.

### Prerequisites

- python3
- pip3

### How To Use

Navigate to the project's root directory.

Install dependencies:

```bash
$ pip3 install -r requirements.txt
```

Change token_id and token in [personal_access_token.py](./personal_access_token.py):

```python
token_id = 'YOUR_SIPGATE_TOKEN_ID'
token = 'YOUR_SIPGATE_TOKEN'
```

Run the application:

```bash
$ python3 personal_access_token.py
```

### How It Works

Request parameters like url and headers are defined as follows:

```python
base_url = 'https://api.sipgate.com/v2'
token_id = 'YOUR_SIPGATE_TOKEN_ID'
token = 'YOUR_SIPGATE_TOKEN'

credentials = (token_id + ':' + token).encode('utf-8')
base64_encoded_credentials = base64.b64encode(credentials).decode('utf-8')

headers = {
    'Authorization': 'Basic ' + base64_encoded_credentials
}
```

**Note:** Basic Auth requires the credentials to be Base64-encoded.  
**Note:** The base64 encoder requires byte-like-objects. We use `.encode('utf-8')` and `.decode('utf-8')` to convert strings to byte-like-objects and vice versa.

> If OAuth should be used for `Authorization` instead of Basic Auth we do not suply the auth object in the request options. Instead we set the authorization header to `Bearer` followed by a space and the access token: `` Authorization: `Bearer ${accessToken}`, ``. For an example application interacting with the sipgate API using OAuth see our [sipgate.io python OAuth example](https://github.com/sipgate-io/sipgateio-oauth-python).

---

We use the python package 'requests' for request generation and execution.
The requested URL consists of the base url defined above and the endpoint `/account`.
This example prints the status code and response body to the console.

```python
response = requests.get(base_url + '/account', headers=headers)

print('Status:', response.status_code)
print('Body:', response.content.decode("utf-8"))
```

### Common Issues

#### HTTP Errors

| reason                          | errorcode |
| ------------------------------- | :-------: |
| token_id and/or token are wrong |    401    |
| credentials not Base64-encoded  |    401    |
| wrong REST API endpoint         |    404    |
| wrong request method            |    405    |

### Related

- [requests documentation](http://docs.python-requests.org/en/master/)
- [base64 documentation](https://docs.python.org/3/library/base64.html)

### Contact Us

Please let us know how we can improve this example.
If you have a specific feature request or found a bug, please use **Issues** or fork this repository and send a **pull request** with your improvements.

### License

This project is licensed under **The Unlicense** (see [LICENSE file](./LICENSE)).

### External Libraries

This code uses the following external libraries

- requests:  
   Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)  
   Website: http://docs.python-requests.org/en/master/

---

[sipgate.io](https://www.sipgate.io) | [@sipgateio](https://twitter.com/sipgateio) | [API-doc](https://api.sipgate.com/v2/doc)
