import os
import subprocess


def serve(path):
    os.chdir("Projects/"+path+"/www")
    serv = subprocess.Popen(["python3", "-m", "http.server", "8080", "--bind", "127.0.0.1"])

    while 1:
        x = input("press q to exit\n")
        if x == 'q':
            break

    serv.kill()