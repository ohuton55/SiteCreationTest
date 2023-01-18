import requests

host = 'http://time.imodurushiki.com/'

res = requests.get(host)
print(res.headers)
