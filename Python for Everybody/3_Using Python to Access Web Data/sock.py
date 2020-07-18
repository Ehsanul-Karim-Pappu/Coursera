# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# # cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# # cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# # here encode() just encode the Unicode str to UTF8.so I can replace it with b'str' as UTF8 are bytes
# cmd = b'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'
# mysock.send(cmd)

# c = 0
# while True:
#     data = mysock.recv(550)
#     if (len(data) < 1):
#         break
#     print(data.decode())
#     c += 1
# mysock.close()
# print(c)


# An easy version of the above code is -

import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
