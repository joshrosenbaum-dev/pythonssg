import markdown
import os
import shutil

def mdConvert(src, www):
    srcpath = src # /Projects/tempProject
    wwwpath = www # /Projects/tempProject_www

    for filename in os.listdir(srcpath):
        if filename.endswith(".md"):
            input_file = open(srcpath +"/" + filename)
            text = input_file.read()
            html = markdown.markdown(text)
            os.mkdir(wwwpath + "/" + filename.replace(".md", ""))
            output_file = open(wwwpath + "/" + filename.replace(".md", "") + "/" + "index.html", "w")
            output_file.write(html)
            print("Converted MD (.md) files are now in web directory!")
            continue
        else:
            continue
