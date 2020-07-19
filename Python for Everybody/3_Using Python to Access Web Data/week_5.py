from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

xml = urlopen(input(), context=ctx).read()
# print(xml.decode())  
tree = ET.fromstring(xml)
counts = tree.findall('comments/comment')
print(len(counts))
s = 0
for item in counts:
    # print(item.find('count').text)
    s += int(item.find('count').text)

print(s)

#######just for checking the sum###########
# import re

# n = re.findall('<count>([0-9]+)</count>', xml.decode())
# a = list(map(int, n))
# print(sum(a))