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


appId = '' # 填入AppID
masterKey = '' # 填入MasterKey
data = {"content": "{{subinput}}"}

headers = {
    'Content-Type': 'application/json',
    'X-LC-Id': appId,   
    'X-LC-Key': '{},master'.format(masterKey)
}

# 以下链接只使用于国际版，国内域名会不一样，需要去设置页面找一下
url = 'https://{}.api.lncldglobal.com/1.1/classes/content'.format(appId[:8])

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
appId = '' # 填入AppID
masterKey = ''   # 填入masterKey
timestamp = int(round(time.time() * 1000))

ret = str(timestamp)+masterKey

sign = hashlib.md5(ret.encode('utf-8')).hexdigest()

headers = {
    'Content-Type': 'application/json',
    'X-LC-Id': appId,
    'X-LC-Sign': "{},{},master".format(sign,timestamp)
}

# 以下链接只使用于国际版，国内域名会不一样，需要去设置页面找一下
url = 'https://{}.api.lncldglobal.com/1.1/classes/content'.format(appId[:8])

http = urllib3.PoolManager(timeout = 3)

r = http.request('POST', url, body=json.dumps(data), headers = headers)

if str(r.status) == "201":
    print('success!')
    print(json.loads(r.data.decode('utf-8')))
else:
    print('fail!')
    print(json.loads(r.data.decode('utf-8')))

```
