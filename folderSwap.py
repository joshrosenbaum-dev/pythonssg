import os
import shutil

wwwpath = os.getcwd() + "/www"
tmppath = os.getcwd() + "/www_tmp"

if os.path.exists(tmppath):
    shutil.rmtree(tmppath)

if os.path.exists(wwwpath):
    shutil.copytree(wwwpath, tmppath)
    shutil.rmtree(wwwpath)
    os.rename(tmppath, wwwpath)
else:
    os.mkdir(wwwpath)