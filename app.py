from src import app
from threading import Thread
from flask_socketio import SocketIO, send
from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args,directory=r'C:\Users\makn0023\Desktop\copy>',**kwargs)

def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('localhost', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

socketio = SocketIO(app)
if __name__ == '__main__':
    Thread(target=run, daemon=True).start()
    socketio.run(app, port=8080, debug=True)