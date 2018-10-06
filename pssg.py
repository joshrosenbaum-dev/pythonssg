# PSSG.py - CLI driver for Pumpkin Spice Static Site Generator

import argparse
import os
import simpleBuild
import localserv


def main():
    parser = argparse.ArgumentParser(description="PSSG CLI")

    # Arguments go here cmd group is mutually exclusive
    cmd = parser.add_mutually_exclusive_group()
    cmd.add_argument('-n', '--new', help="new project", action='store', dest='newfile')
    cmd.add_argument('-b', '--build', help="build project", action='store', dest='buildfile')
    parser.add_argument('-s', '--serve', help="start preview server", action='store_true')
    # parser.add_argument('-f', '-filename', help="name of project folder", action='store', dest='filename')

    args = parser.parse_args()

    # basic calls based on arguments run 'python PSSG.py -h' for usage
    if args.newfile:
        if not os.path.exists(os.path.join(os.getcwd(), "Projects", args.newfile)):
            print("[OK] Making new project titled " + args.newfile + ".")
            os.makedirs(os.path.join(os.getcwd(), "Projects", args.newfile, "src"))
            print("[OK] Project folder generated.")
        else:
            print("[ERROR] This project already exists!")

    elif args.buildfile:
        projName = args.buildfile
        projPath = os.path.join(os.getcwd(), "Projects", projName)
        simpleBuild.build(projPath)
        if args.serve:
            print("starting preview server")
            localserv.serve(args.buildfile)
    else:
         parser.print_help()


if __name__ == "__main__":
    main()
