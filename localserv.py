# webtest.py
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import webbrowser


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        print("do_get")
        if self.path == '/':
            self.path = '/index.html'
        try:
            page = open(self.path[1:]).read()
            self.send_response(200)
        except:
            page = "Page not Found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(page, 'utf-8'))


def preview_site(path):
    os.chdir(path)
    httpd = HTTPServer(('localhost', 8080), Server)
    # webbrowser.open('localhost:8080', new=0, autoraise=True)
    httpd.serve_forever()

    # previewSite("/home/beanz/cs370/folder/")
