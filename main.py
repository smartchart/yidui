# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:48:44 2020

@author: Administrator
"""

import random
import string
from requests.packages import urllib3
import requests
from yd import send_message, login_get_parameter

'''
生成随机设备信息
'''
device_token = ''.join(random.sample(string.ascii_letters + string.digits, 50))  # 生成随机得devicetoken
unique_id = ''.join(random.sample(string.ascii_letters + string.digits, 32))  # 生成随机 unique_id
headers = {
    "DeviceToken": device_token,
    "Memberid": "",
    "Authorization": "",
}
if __name__ == '__main__':
    mobile = input("请输入手机号:")
    r = send_message(mobile, headers)
    print(r)
    code = input("请输入验证码:")
    member_id, authorization = login_get_parameter(mobile, code, unique_id, headers)
    print('memberid:{}'.format(member_id))
    print('authorization:{}'.format(authorization))
    url = 'https://api.520yidui.com/v2/members/list?page=1&category=home&devicetoken=' + device_token
    headers['Memberid'] = member_id
    headers['Authorization'] = authorization
    urllib3.disable_warnings()
    r = requests.get(url, {}, headers=headers, verify=False).json()
    print(r)
