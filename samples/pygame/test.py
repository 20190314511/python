# 演示获取机器名称和时间
import socket

name=socket.gethostname()
ip = socket.gethostbyname(name)

# 演示获取操作系统名称
import platform
osname = platform.platform()

# 演示获取系统时间
import datetime
now = datetime.datetime.now()

# 打印获取的信息
print(name, ip)
print(osname)
print(now)
