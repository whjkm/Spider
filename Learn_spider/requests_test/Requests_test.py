# requests
# 实例引入
'''
import requests
response = requests.get('https://www.baidu.com')
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
'''
from requests import ReadTimeout

'''
# 各种请求方法
import requests
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/get')
requests.options('http://httpbin.org/get')
'''

# 请求
# 基本GET请求
# 基本写法
'''
import requests
response = requests.get('http://httpbin.org/get')
print(response.text)
'''

# 带参数GET请求
'''
import requests
response = requests.get('http://httpbin.org/get?name=gemey&age=22')
print(response.text)
'''

'''
import requests
data = {
    'name': 'gemey',
    'age': '22'
}
response = requests.get('http://httpbin.org/get', params=data)
print(response.text)
'''

# 解析json
'''
import requests
import json
response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
'''

# 获取二进制数据
'''
import requests
response = requests.get('https://github.com/favicon.ico')
print(type(response.text), type(response.content))
print(response.text)
print(response.content)
'''

'''
import requests
response = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(response.content)
    f.close()
'''

# 添加headers
'''
import requests
response = requests.get('https://www.zhihu.com/explore')
print(response.text)
'''
'''
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}
response = requests.get('https://www.zhihu.com/explore', headers=headers)
print(response.text)
'''

# 基本POST请求
'''
import requests
data = {
    'name': 'gemey',
    'age': '22'
}
response = requests.post('http://httpbin.org/post', data=data)
print(response.text)
'''
'''
import requests
data = {
    'name': 'gemey',
    'age': '22'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}
response = requests.post('http://httpbin.org/post', data=data, headers=headers)
print(response.json())
'''

# 响应
# response属性
'''
import requests
response = requests.get('http://www.jianshu.com')
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)
'''
'''
# 状态码判断
import requests
response = requests.get('http://www.jianshu.com')
exit() if not response.status_code == requests.codes.ok else print('Request Successfully')

import requests
response = requests.get('http://www.jianshu.com')
exit() if not response.status_code == 200 else print('Request Successfully')
'''
'''
import requests
response = requests.get('http://www.jianshu.com/hello.html')
exit() if not response.status_code == requests.codes.not_found else print('404 Not Found')
'''

# 高级操作
# 文件上传
'''
import requests
files = {
    'file': open('favicon.ico', 'rb')
}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)
'''

# 获取cookie
'''
import requests
response = requests.get('http://www.baidu.com')
print(response.cookies)
for key, value in response.cookies.items():
    print(key + "=" + value)
'''

# 会话维持
# 模拟登陆
'''
import requests
requests.get('http://httpbin.org/cookies/set/number/123456789')
response = requests.get('http://httpbin.org/cookies')
print(response.text)
'''
'''
import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)
'''
# 证书验证
'''
import requests
response = requests.get('https://www.12306.cn')
print(response.status_code)
'''
'''
import requests
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
'''

'''
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
'''

# 代理设置
'''
import requests
proxies = {
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743',
}
response = requests.get('https://www.taobao.com', proxies=proxies)
print(response.status_code)
'''
'''
import requests
proxies = {
    'http': 'http://user:password@127.0.0.1:9743/',

}
response = requests.get('https://www.taobao.com', proxies=proxies)
print(response.status_code)
'''
# socks代理
'''
import requests
proxies = {
    'http': 'socks5://127.0.0.1:9742',
    'https': 'socks5://127.0.0.1:9742',
}
response = requests.get('https://www.taobao.com', proxies=proxies)
print(response.status_code)
'''

# 超时设置
'''
import requests
response = requests.get('https://httpbin.org', timeout=1)
print(response.status_code)
'''
'''
import requests
from requests.exceptions import ReadTimeout
try:
    response = requests.get('https://httpbin.org/get', timeout=1)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
'''

# 认证设置
'''
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://120.27.34.24:9007', auth=HTTPBasicAuth('user', '123'))
print(r.status_code)
'''
'''
import requests

r = requests.get('http://120.27.34.24:9007', auth=('user', '123'))
print(r.status_code)
'''

# 异常处理
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException

try:
    response = requests.get('http://httpbin.org/get', timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')




