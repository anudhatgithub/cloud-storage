import dropbox
import os

acctoken = "asdwfghjbaoutbo"
db = dropbox.Dropbox("awbdrfoiwabrfoi3qwboifboqaiw")

path = "C:/Users/Happy/Downloads/PRO-C40-master/PRO-C40-master"
filelist = os.listdir(path)
for file in filelist:
    print("C:/Users/Happy/Downloads/PRO-C40-master/PRO-C40-master/"+file)

    upfile = open("C:/Users/Happy/Downloads/PRO-C40-master/PRO-C40-master/"+file,"rb").read()
    db.files_upload(upfile,"/PRO-C40-master/"+file,mode=dropbox.files.WriteMode.overwrite)
