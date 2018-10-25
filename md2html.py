import markdown
import os
import shutil

def mdConvert(src, www):

        for filename in os.listdir(src):
            try:
                if filename.endswith(".md") and filename != "masterindex.md":
                    input_file = open(src +"/" + filename)
                    text = input_file.read()
                    html = markdown.markdown(text)
                    os.mkdir(www + "/" + filename.replace(".md", ""))
                    output_file = open(www + "/" + filename.replace(".md", "") + "/" + "index.html", "w")
                    output_file.write(html)
                    print("[OK] Converted MD (.md) files are now in web directory!")
                    continue
                elif filename == "masterindex.md":
                    input_file = open(src +"/" + filename)
                    text = input_file.read()
                    html = markdown.markdown(text)
                    output_file = open(www +'/' + "index.html", "w")
                    output_file.write(html)
                else:
                    continue
            except:
                print("[ERROR] " +filename + " is not a valid markdown file, Fix and rebuild")
                continue
