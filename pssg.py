# PSSG.py - CLI driver for Pumpkin Spice Static Site Generator

import argparse
import os
import simpleBuild
import localserv


def main():
    parser = argparse.ArgumentParser(description="PSSG CLI")

    # Arguments go here cmd group is mutually exclusive
    cmd = parser.add_mutually_exclusive_group()
    cmd.add_argument('-n', '--new', help="create new project", action='store', dest='newfile')
    cmd.add_argument('-S', '--startserver', help="start preview server at project path", action='store', dest='project')
    parser.add_argument('-s', '--serve', help="start preview server after building", action='store_true')
    cmd.add_argument('-b', '--build', help="build project", action='store', dest='buildfile')

    # parser.add_argument('-f', '-filename', help="name of project folder", action='store', dest='filename')

    args = parser.parse_args()

    # basic calls based on arguments run 'python PSSG.py -h' for usage
    if args.newfile:
        if not os.path.exists(os.path.join(os.getcwd(), "Projects", args.newfile)):
            print("[OK] Making new project titled " + args.newfile + ".")
            os.makedirs(os.path.join(os.getcwd(), "Projects", args.newfile, "src"))

            tmpFile = open(os.path.join("Projects/" + args.newfile + "/"+"src/", "masterindex.md"), "w+")
            tmpFile.write('''<meta http-equiv="refresh" content="0; URL='http://localhost:8080/home/'" />''')
            tmpFile.close()

            print("[OK] Project folder generated.")
        else:
            print("[ERROR] This project already exists!")

    elif args.buildfile:
        projName = args.buildfile
        projPath = os.path.join(os.getcwd(), "Projects", projName)
        simpleBuild.build(projPath)
        if args.serve:
            print("[OK] Starting Preview Server")
            localserv.serve(args.buildfile)
    elif args.project:
        if os.path.exists(os.path.join(os.getcwd(), "Projects", args.project)):
            print("[OK] Starting Preview Server")
            localserv.serve(args.project)
        else:
            print("[ERROR] Project cannot be found!")
    else:
         parser.print_help()


if __name__ == "__main__":
    main()
