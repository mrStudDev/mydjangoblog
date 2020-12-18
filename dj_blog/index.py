from http.server import BaseHTTPRequestHandler
from cowpy import cow

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.Posts
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return
