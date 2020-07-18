from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input()
c = int(input())
pos = int(input())
j = 1
for i in range(c):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.findAll('a'):
        if j == pos:
            print(tag.contents[0])
            url = tag.get('href', None)
            j = 1
            break
        j += 1
