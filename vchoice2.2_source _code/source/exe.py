import time

time.localtime(time.time())

print(time.strftime('%Y_%m_%d',time.localtime(time.time())))