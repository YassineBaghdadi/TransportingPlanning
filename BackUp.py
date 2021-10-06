import json, os, pymysql
import subprocess
import time

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth



server = json.load(open(os.path.join(os.getcwd(), "server.json")))
host = server["host"]
user = server["user"]
database = server["db"]
psswrd = server["password"]
port = server["port"]



def con():
    return pymysql.connect(host=host, user=user, database=database, password=psswrd, port=port)


os.popen(f"mysqldump -h 10.73.100.101 -P 3306 -u VP -p1234@@it. vansplanning > STM_backUp_{time.strftime('%Y-%m-%d %H:%M:%S')}.sql" )


gauth = GoogleAuth()


gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)





f = drive.CreateFile({'title': "test"})
f.SetContentFile(os.path.join(os.getcwd(), "saccomxd.png"))
f.Upload()
