# Simple Website Building
# Author: Josh Rosenbaum, 09/27/2018

# Concept: To generate the website package for the user, swap and update the project on continued basis.
#          Module invoked by command line with argument: `-b or --build projectNameHere`

import os
import shutil

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
        print("[OK] Initialized project website package")
    else:
        print("[OK] Package already exists. Regenerating project website package")
        os.makedirs(newPath)
        tmpFile = open(os.path.join(newPath, "file.html"), "w")
        tmpFile.write("<h1>Hello, Starbucks.</h1><p>Temporary</p>")
        tmpFile.close()
        os.renames(pkgPath, tmpPath)
        os.renames(newPath, pkgPath)
        shutil.rmtree(tmpPath)

projPath = os.path.join(os.getcwd(), "Projects", "testProject") # Replicating CLI
build(projPath)