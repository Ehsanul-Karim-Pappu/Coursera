from urllib.request import urlopen
import urllib.parse
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

parms = dict()
parms['address'] = input()
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

jsn = urlopen(url, context=ctx).read()

jsn = json.loads(jsn)
# print(json.dumps(jsn, indent=4))

print(jsn['results'][0]['place_id'])
