import os
import markdown

def md2html(filename):
	"Takes a mardown file and converts it to html"

	file = open(filename,"r")

	html = markdown.markdown(file.read())

	newfile = open("Test.html","w")

	newfile.write(html)

	file.close()
	newfile.close()
	
	return "Success!"

filename = input("Enter a file name: ")
md2html(filename)

