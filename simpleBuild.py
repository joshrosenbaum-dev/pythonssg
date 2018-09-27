# Simple Website Creation
# 9/27/18
# Author:   Josh Rosenbaum
#
# Concept:  To generate the website package for the user to upload freely.
#           Module invoked by command line with argument:
#           `-b or --build projectNameHere`
#


import os

pkgPath = os.path.join(os.getcwd(), "www")
print(pkgPath)