from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
import ssl
# import socket

class Mkokm(BaseHTTPRequestHandler):

    # def handle(self):
    #     print( dir( self ) ) 
        # self.send_response(200, b'Hello, world from handle!')
        # self.end_headers()
        # self.wfile.write(b'Hello, world from handle!')
    def do_CONNECT(self):
        print('aoskaosk')
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, wzxzxrld sndjksnd ')
    def do_PUT(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, wzxzxrld!')
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"""<!DOCTYPE html>
                        <html>
                        <head>
                        <meta charset="UTF-8">
                        <link rel="icon" href="data:;base64,iVBORw0KGgo=">
                        <title>Title of the document</title>
                        </head>

                        <body>
                        Content of the document......
                        </body>

                        </html>""")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('127.0.0.1', 8020), Mkokm)
httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="./pri.key", 
        certfile='./cer.cert', server_side=True)

httpd.serve_forever()