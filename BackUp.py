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

filename = f"STM_backUp_{time.strftime('%Y%m%d%H%M%S')}.sql"
os.popen(f"mysqldump -h {host} -P {port} -u VP -p{psswrd} {database} > {filename}" )


gauth = GoogleAuth()


gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': filename})
f.SetContentFile(os.path.join(os.getcwd(), filename))
f.Upload()
# time.sleep(2)
# os.remove(filename)
# os.replace(filename, f"/home/yassinebaghdadi/Desktop/STM_backup/{filename}")

