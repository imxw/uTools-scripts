#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

data = {"content": "{{subinput}}"}

headers = {
    'Content-Type': 'application/json',
    'X-LC-Id': '',   # 填入AppID
    'X-LC-Key': ',master' # 逗号前填入masterKey
}

url = 'https://AppID前八位.api.lncldglobal.com/1.1/classes/content'

http = urllib3.PoolManager(timeout = 3)

r = http.request('POST', url, body=json.dumps(data), headers = headers)

if str(r.status) == "201":
    print('success!')
    print(json.loads(r.data.decode('utf-8')))
else:
    print('something is wrong!')

