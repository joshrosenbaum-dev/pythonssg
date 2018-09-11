import os
import shutil

srcpath = os.getcwd() + "/src"
tmppath = os.getcwd() + "/tmp"

if os.path.exists(tmppath):
    shutil.rmtree(tmppath) # removes tmp if it exists already for backup

elif os.path.exists(srcpath):
    shutil.copytree(srcpath, tmppath) # copies the original folder
    shutil.rmtree(tmppath) # deletes the tmp folder
    os.rename(tmppath, srcpath) # renames tmp to src for viewing
else:
    os.mkdir(srcpath)