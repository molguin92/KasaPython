#!/usr/bin/env python3
from get_token import *
import click


@click.group()
def control():
    pass


@control.command('DeviceList')
def getDeviceList() -> None:
    params = {'token': getKasaAPIToken()}

    resp = req.post(KASA_URL, params=params, json=KASA_DVC_LIST_REQ)
    devices = resp.json()['result']['deviceList']
    print(resp.json())

    print('{:40s} \t {:40s} \t {:40s}'.format('Device', 'Model', 'ID'))
    for dev in devices:
        print('{:40s} \t {:40s} \t {:40s}'.format(dev['alias'],
                                                  (dev['deviceModel'] + ' ' +
                                                   dev['deviceName']),
                                                  dev['deviceId']))


@control.command('TurnOff')
@click.argument('device')
def turnOff(device: str) -> None:
    KASA_REQ_DATA_DVC_CONTROL['system']['set_relay_state']['state'] = 0
    KASA_DVC_CONTROL_REQ['params']['deviceId'] = device
    KASA_DVC_CONTROL_REQ['params'] \
        ['requestData'] = json.dumps(KASA_REQ_DATA_DVC_CONTROL)

    params = {'token': getKasaAPIToken()}
    resp = req.post(KASA_APP_SERVER_URL,
                    params=params, json=KASA_DVC_CONTROL_REQ)


@control.command('TurnOn')
@click.argument('device')
def turnOn(device: str) -> None:
    KASA_REQ_DATA_DVC_CONTROL['system']['set_relay_state']['state'] = 1
    KASA_DVC_CONTROL_REQ['params']['deviceId'] = device
    KASA_DVC_CONTROL_REQ['params'] \
        ['requestData'] = json.dumps(KASA_REQ_DATA_DVC_CONTROL)

    params = {'token': getKasaAPIToken()}
    resp = req.post(KASA_APP_SERVER_URL,
                    params=params, json=KASA_DVC_CONTROL_REQ)


if __name__ == '__main__':
    control()
