import os
import hashlib


# Creates Hash of File
def md5(fname):
    hash_sha256 = hashlib.sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


# Recursively obtains all files in directory
def rhash(directory):
    with open("md5list.txt", "w+"):
        with open("md5list.txt", "a") as cs:
            for root, dirs, files in os.walk(directory, topdown=True):  # File Path
                for name in files:
                    var = os.path.join(root, name)
                    print(var, file=cs)
                    print(md5(var), file=cs)