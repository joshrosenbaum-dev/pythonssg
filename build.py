import os
import shutil
import markdown

srcpath = os.getcwd() + "/src/"
wwwpath = os.getcwd() + "/www"
tmppath = os.getcwd() + "/www_tmp"

if os.path.exists(tmppath):
    shutil.rmtree(tmppath)

if os.path.exists(wwwpath):
    shutil.copytree(wwwpath, tmppath)
    shutil.rmtree(wwwpath)
    os.rename(tmppath, wwwpath)
else:
    os.mkdir(wwwpath)

for filename in os.listdir(srcpath):
    if filename.endswith(".md"):
        input_file = open(srcpath + filename)
        text = input_file.read()
        html = markdown.markdown(text)
        os.mkdir(wwwpath + "/" + filename.replace(".md", ""))
        output_file = open(wwwpath + "/" + filename.replace(".md", "") + "/" + "index.html", "w")
        output_file.write(html)
        print("Converted!")
        continue
    else:
        continue