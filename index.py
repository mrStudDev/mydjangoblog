from http.server import BaseHTTPRequestHandler
from cowpy import cow

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_Posts()
        elf.send_dj_blog()
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return


