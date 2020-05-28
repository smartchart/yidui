# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:35:17 2020

"""

import requests
from requests.packages import urllib3


def send_message(mobile, headers):
    data = {
        "hard_code": 1,
        "phone": mobile,
        "sign": "9f8ab72be23941e98b7e6757d8c16663",
        "timestamp": "1590646041.463563"
    }
    urllib3.disable_warnings()
    r = requests.put("https://api.520yidui.com/v2/auths/send_captcha.json", data, headers=headers, verify=False).text
    return r


def login_get_parameter(mobile, code, unique_id, headers):
    data = {
        "captcha": code,
        "hard_code": "1",
        "phone": mobile,
        "unique_id": unique_id
    }

    urllib3.disable_warnings()
    r = requests.post("https://api.520yidui.com/v2/auths/phone_auth.json", data, headers=headers, verify=False).json()
    Memberid = r['id']
    token = r['token']
    data = {
        "code": token,
        "id": Memberid,
        "info%5Bdevice_id%5D": "",
        "info%5Bmac%5D": ""
    }
    urllib3.disable_warnings()
    r = requests.post("https://api.520yidui.com/v2/login", data, headers=headers, verify=False).json()
    Authorization = r['token']
    return Memberid, Authorization
