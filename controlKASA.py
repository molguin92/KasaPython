#!/usr/bin/env python3
from get_token import *
import click


@click.group()
def control():
    pass


@control.command('DeviceList')
def getDeviceList() -> None:
    token = getKasaAPIToken()
    params = {'token': token}

    resp = req.post(KASA_URL, params=params, json=KASA_DVC_LIST_REQ)
    devices = resp.json()['result']['deviceList']

    print('{:40s} \t {:40s} \t {:40s}'.format('Device', 'Model', 'ID'))
    for dev in devices:
        print('{:40s} \t {:40s} \t {:40s}'.format(dev['alias'],
                                                  (dev['deviceModel'] + ' ' +
                                                   dev['deviceName']),
                                                  dev['deviceId']))


if __name__ == '__main__':
    control()
