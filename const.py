KASA_URL = 'https://wap.tplinkcloud.com'
KASA_DVC_LIST_REQ = {'method': 'getDeviceList'}
KASA_APP_SERVER_URL = 'https://eu-wap.tplinkcloud.com'
KASA_DVC_CONTROL_REQ = {
    'method': 'passthrough',
    'params': {
        'deviceId': None,
        'requestData': None
    }
}

KASA_REQ_DATA_DVC_CONTROL = {
    'system': {
        'set_relay_state': {
            'state': None
        }
    }
}
