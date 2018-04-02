import requests as req
import json
import uuid

KASA_URL = 'https://wap.tplinkcloud.com'

def getKasaAPIToken() -> str:
    # get a random uuid4 as client id
    client_id = str(uuid.uuid4())

    # POST to the Kasa API and get a token
    # read credentials from credentials.json

    with open('credentials.json', 'r') as credentials_f:
        credentials = json.loads(credentials_f.read())

    payload = {
        'method': 'login',
        'params': {
            'appType'      : 'Kasa_Android',
            'cloudUserName': credentials['user_name'],
            'cloudPassword': credentials['password'],
            'terminalUUID' : client_id
        }
    }

    resp = req.post(KASA_URL, json=payload)
    resp_j = resp.json()
    return resp_j['result']['token']

if __name__ == '__main__':
    token = getKasaAPIToken()
    with open('.token', 'w') as token_f:
        token_f.write(token)
        token_f.write('\n')

