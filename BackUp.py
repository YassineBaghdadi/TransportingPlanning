from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

# For using listdir()
import os

# Below code does the authentication
# part of the code
gauth = GoogleAuth()


gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)



f = drive.CreateFile({'title': "test"})
f.SetContentFile(os.path.join(os.getcwd(), "saccomxd.png"))
f.Upload()
