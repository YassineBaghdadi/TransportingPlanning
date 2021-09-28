#-------------------------------------------------------------------------------
# Imports
import pyrebase
import os, ntpath

#-------------------------------------------------------------------------------
# Variables & Setup

# filelist = [ f for f in os.listdir(".") if f.endswith(".JPG") ]
# for f in filelist:
#     os.remove(os.path.join(".", f))

config = {
"apiKey": "AIzaSyAIV0qDv7WI3kU_krALZEc-PlTCkBRMp9g",
"authDomain": "saccomxd-stm-yassine-baghdadi.firebaseapp.com",
"databaseURL": "https://saccomxd-stm-yassine-baghdadi-default-rtdb.firebaseio.com",
"projectId": "saccomxd-stm-yassine-baghdadi",
"storageBucket": "saccomxd-stm-yassine-baghdadi.appspot.com",
"serviceAccount": os.path.join(os.getcwd(), "src", "key.json")
}
token = "e230e05d-8b62-4d8b-8b17-56d929d19d54"

#
# #-------------------------------------------------------------------------------
# # Uploading And Downloading Images
#
# storage.child("saccomxd.png").put("saccomxd.png")
# # storage.child("PlayingGuitar.JPG").download("PlayingGuitar.JPG")
#
# all_files = storage.list_files()
#
# for file in all_files:
#     print(file.name)
#     print(storage.child("saccomxd.png").get_url(token))
#     # file.download_to_filename(file.name)

def uploadPic(img : str) -> str:
    if os.path.isfile(img):
        print(f"Local path ==> {img}")
        firebase_storage = pyrebase.initialize_app(config)
        storage = firebase_storage.storage()
        storage.child(ntpath.basename(img)).put(img)
        return storage.child(ntpath.basename(img)).get_url(token)


print(f'pic url ==> {uploadPic(os.path.join(os.getcwd(), "saccomxd.png"))}')