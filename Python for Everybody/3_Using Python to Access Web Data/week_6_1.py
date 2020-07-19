from urllib.request import urlopen
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

jsn = urlopen(input(), context=ctx).read()
# print(jsn.decode())
tree = json.loads(jsn)
print(len(tree['comments']))

s = 0
for item in tree['comments']:
    s += item['count']

print(s)


#######just for checking the sum###########
# import re

# n = re.findall('[0-9]+', jsn.decode())
# a = list(map(int, n))
# print(sum(a))