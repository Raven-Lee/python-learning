from cgitb import reset
from urllib import request, parse

url = 'https://e-hentai.org/'
headers = {
    'User-Agent': 'Mozila/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name':'Germany'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url,  method='get')
r = request.urlopen(url)
print(r.status)
print(r.read().decode('utf-8'))