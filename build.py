import os
import shutil
import markdown
import localserv

srcpath = os.getcwd() + "/src/"
wwwpath = os.getcwd() + "/www"
bkppath = os.getcwd() + "/www_bkp"

def md2html():
    for filename in os.listdir(srcpath):
        if filename.endswith(".md"):
            input_file = open(srcpath + filename)
            text = input_file.read()
            html = markdown.markdown(text)
            os.mkdir(wwwpath + "/" + filename.replace(".md", ""))
            output_file = open(wwwpath + "/" + filename.replace(".md", "") + "/" + "index.html", "w")
            output_file.write(html)
            print("Converted MD (.md) files are now in web directory!")
            continue
        else:
            continue

if not os.path.exists(srcpath):
    os.mkdir(srcpath)
    print("There was no source directory to work with. Please place Markdown (.md) files into the folder named '/src'.")
    exit()

if os.path.exists(bkppath):
    print("Deleting past backups...")
    shutil.rmtree(bkppath)
    print("Done!")

if os.path.exists(wwwpath):
    print("Creating backup...")
    shutil.copytree(wwwpath, bkppath)
    print("Backup created!")
    print("Reinitializing web directory...")
    shutil.rmtree(wwwpath)
    os.mkdir(wwwpath)
    print("Web directory created!")
    md2html()
else:
    print("Initializing web directory...")
    os.mkdir(wwwpath)
    print("Web directory created!")
    md2html()
    
www_redirect = open(wwwpath + "/" + "index.html", "w")
www_redirect.write("<html><head><meta http-equiv='refresh' content='0; url=http://localhost:8080/home'></head></html>")

print("[SUCCESS] Launching web server on localhost:8080")
localserv.preview_site(wwwpath)
