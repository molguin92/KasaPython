import requests as req
from get_token import *

def getDeviceList() -> dict:
    token = getKasaAPIToken()
    params = {'token': token}

    resp = req.post(KASA_URL, params=params, json=KASA_DVC_LIST_REQ)
    return resp.json()

if __name__ == '__main__':
    import pprint
    pprint.PrettyPrinter(indent=4).pprint(getDeviceList())
