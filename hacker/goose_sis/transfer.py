import requests
import json
from lxml import etree

output = open('fanyi.md','a')

url = 'http://139.199.209.106/trans/google.action?from=zh&to=en&query='
f = open('xxx.md','r')
url_transfer = f.read()

print url + url_transfer
r = requests.get(url+url_transfer)
print r.content

output.write(r.content)
output.close()
