# bb
uTools快捷命令中使用的bb脚本

## shell版
### 简单鉴权

```shell
curl -s -X POST "https://AppId前八位.api.lncldglobal.com/1.1/classes/content"  --header "Content-Type: application/json" --header "X-LC-Id: ${AppID}" --header "X-LC-Key: ${masterKey},master" -d "{ \"content\": \"{{subinput}}\" }"

```

### 安全鉴权
有时间再写

## Python版

### 简单鉴权

```python
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
    print('fail!')
    print(json.loads(r.data.decode('utf-8')))
```


### 安全鉴权

```python
#!/usr/local/bin/python3
# _*_ coding: utf-8 _*_

import urllib3
import json
import time
import hashlib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

data = {"content": "{{subinput}}"}
masterKey = ''   # 填入masterKey
timestamp = int(round(time.time() * 1000))

ret = str(timestamp)+masterKey

sign = hashlib.md5(ret.encode('utf-8')).hexdigest()

headers = {
    'Content-Type': 'application/json',
    'X-LC-Id': '', # 填入AppID
    'X-LC-Sign': "{},{},master".format(sign,timestamp)
}

url = 'https://填入AppID前八位.api.lncldglobal.com/1.1/classes/content'

http = urllib3.PoolManager(timeout = 3)

r = http.request('POST', url, body=json.dumps(data), headers = headers)

if str(r.status) == "201":
    print('success!')
    print(json.loads(r.data.decode('utf-8')))
else:
    print('fail!')
    print(json.loads(r.data.decode('utf-8')))

```
