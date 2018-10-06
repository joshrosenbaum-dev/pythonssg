# Simple Website Building
# Author: Josh Rosenbaum, 09/27/2018

# Concept: To generate the website package for the user, swap and update the project on continued basis.
#          Module invoked by command line with argument: `-b or --build projectNameHere`

import os
import shutil
import md2html
import hashing

def build(projPath):
    srcPath = os.path.join(projPath, "src")
    pkgPath = os.path.join(projPath, "www")
    newPath = os.path.join(projPath, "new")
    tmpPath = os.path.join(projPath, projPath + "tmp")

    print("Building website...")
    if not os.path.exists(projPath):
        print("[ERROR] The project you specified doesn't exist!")
        exit(0)
    else:
        print("[OK] Found project directory.")
    if not os.path.exists(pkgPath):
        os.makedirs(pkgPath)
        print("[OK] Initialized project website package.")  # pkgPath created on first run
        md2html.mdConvert(srcPath, pkgPath)
        hashing.rhash(pkgPath)
        print("[OK] Build finished!")
    else:
        print("[OK] Package already exists. Regenerating project website package.")
        os.makedirs(newPath)  # newPath created because pkgPath already exists
        md2html.mdConvert(srcPath, newPath)
        hashing.rhash(newPath)
        os.renames(pkgPath, tmpPath)  # _www is renamed to _tmp
        os.renames(newPath, pkgPath)  # _new is renamed to _www
        shutil.rmtree(tmpPath)  # delete _tmp
        print("[OK] Build finished!")
