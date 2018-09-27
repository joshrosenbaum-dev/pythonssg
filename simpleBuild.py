# Simple Website Creation
# Author: Josh Rosenbaum, 09/27/2018

# Concept: To generate the website package for the user to upload freely.
#          Module invoked by command line with argument: `-b or --build projectNameHere`
#

import os

def build(projPath):
    pkgPath = os.path.join(projPath, projPath + "_www")
    print(pkgPath)

projPath = os.path.join(os.getcwd(), "Projects", "testProject") # Replicating CLI
build(projPath)