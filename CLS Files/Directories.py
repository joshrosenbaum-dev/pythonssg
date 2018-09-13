import os
import shutil

#Testing File for os and shutil functions in the manipulation of file directories.

#Absolute Directory - Absolute is not found so is created.
newpath = r'/home/lee/Desktop/CS370 Python SSG/Absolute'

if not os.path.exists(newpath):
    os.makedirs(newpath)

#Indirect Directory - Indirect found or not is overwritten based on that file structure
dir = 'Indirect/Sub-folder'

if os.path.exists(dir):
    shutil.rmtree(dir)
    os.makedirs(dir)
else:
    os.makedirs(dir)

dir = '../Tester'
os.makedirs(dir)

