print("20190314546 李吉洁")     # 具体学号姓名请用自己信息代替

import socket
NAME=socket.gethostname()
IP = socket.gethostbyname(NAME)

import platform
OSNAME=platform.platform()

import datetime
NOW=datetime.datetime.now()

print(NAME, IP)
print(OSNAME)
print( NOW )