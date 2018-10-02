# Simple Website Building
# Author: Josh Rosenbaum, 09/27/2018

# Concept: To generate the website package for the user, swap and update the project on continued basis.
#          Module invoked by command line with argument: `-b or --build projectNameHere`

import os
import shutil
import md2html

def build(projPath):
    pkgPath = os.path.join(projPath, projPath + "_www")
    newPath = os.path.join(projPath, projPath + "_new")
    tmpPath = os.path.join(projPath, projPath + "_tmp")

    print("Building website...")
    if not os.path.exists(projPath):
        print("[ERROR] The project you specified doesn't exist!")
        exit(0)
    else:
        print("[OK] Found project directory")
    if not os.path.exists(pkgPath):
        os.makedirs(pkgPath)
        print("[OK] Initialized project website package")  # pkgPath created on first run
        #TODO: md2html goes here
        md2html.mdConvert(projPath, newPath)
        print("[OK] Build finished!")
    else:
        print("[OK] Package already exists. Regenerating project website package")
        os.makedirs(newPath)  # newPath created because pkgPath already exists
        tmpFile = open(os.path.join(newPath, "file.html"), "w")
        tmpFile.write("<h1>Hello, Starbucks.</h1><p>Temporary</p>")
        tmpFile.close()  # file is place in newPath to show a change in file structure vs. empty test case
        # TODO: md2html goes here, above lines removed
        md2html.mdConvert(projPath, newPath)
        os.renames(pkgPath, tmpPath)  # _www is renamed to _tmp
        os.renames(newPath, pkgPath)  # _new is renamed to _www
        shutil.rmtree(tmpPath)  # delete _tmp
        print("[OK] Build finished!")

# projPath = os.path.join(os.getcwd(), "Projects", "testProject") # Replicating CLI
# build(projPath)
