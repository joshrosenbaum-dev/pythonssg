#PSSG.py - CLI driver for Pumpkin Spice Static Site Generator

import argparse
import os
import simpleBuild

def main():
    parser = argparse.ArgumentParser(description="PSSG CLI")

    #Arguments go here cmd group is mutually exclusive
    cmd = parser.add_mutually_exclusive_group()
    cmd.add_argument('-n','--new',help="new project",action='store_true')
    cmd.add_argument('-b','--build',help="build project", action='store_true')
    parser.add_argument('-s','--serve',help="start preview server",action='store_true')
    parser.add_argument('-f','-filename',help="name of project folder", action='store', dest='filename')

    args = parser.parse_args()

    #basic calls based on arguments run 'python PSSG.py -h' for usage
    if args.new:
        print("Making new project: "+args.filename)
        #TODO: call new project function
    elif args.build:
        projName = args.filename
        projPath = os.path.join(os.getcwd(), "Projects", projName)
        simpleBuild.build(projPath)
        if args.serve:
            print("starting preview server")
            #TODO: call server function


if __name__ == "__main__":
    main()