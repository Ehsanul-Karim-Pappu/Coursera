from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen(input(), context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')

c, s = 0, 0
# for tag in tags:
#     s += int(tag.contents[0])
#     c += 1
##### same ######
for i in soup.find_all('span'):
    s += int(i.contents[0])
    c += 1

print('Count %d' % c)
print('Sum %d' % s)
