from urllib.request import urlopen
from bs4 import BeautifulSoup
# for handling 104 error
from socket import error as SocketError
import errno
import urllib.parse
import re
import ssl
import os

# code to avoid SSL certificate error
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

main_url = 'https://www.py4e.com/code3/'
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'

req = urllib.request.Request(main_url, headers=headers)
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.findAll('a'):
    if re.search('.*\.(py|txt|html)$', tag.contents[0]):
        try:
            url = main_url + tag.get('href', None)
            headers = {}
            headers['User-Agent'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'
            req = urllib.request.Request(url, headers=headers)
            code = urlopen(req).read().decode('utf8')
            filename = "code/" + tag.contents[0]
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as fhand:
                fhand.write(code)
                fhand.close()
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise  # Not error we are looking for
            pass  # Handle error here.
