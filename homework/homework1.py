print("20190314546 李吉洁")     # 具体学号姓名请用自己信息代替

import socket
name=socket.gethostname()
ip = socket.gethostbyname(name)

import platform
osname=platform.platform()

import datetime
now=datetime.datetime.now()

print(name, ip)
print(osname)
print( now )