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

REQ_DATA_SET_STATE = {
    'system': {
        'set_relay_state': {
            'state': None
        }
    }
}

REQ_DATA_GET_INFO = {
    'system': {'get_sysinfo': None},
    'emeter': {'get_realtime': None}
}
