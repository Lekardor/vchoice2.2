import os
import datetime
def worker(kind='maoyan',minutes=30,driverPath='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'):
#3 parameters 
#kind is the web you want to get data from, maoyan and baidu
#minutes is the frequency
#driverPath is the path of chromedriver
#if you want to stop, the only way you can do is exit cmd
    try:
        print("start  python reptile.py "+kind+' '+str(minutes)+' '+driverPath)
        os.system("start  python reptile.py "+kind+' '+str(minutes)+' 2015 2018 '+driverPath)
    except KeyboardInterrupt:
        print('exit time:', datetime.datetime.now())


