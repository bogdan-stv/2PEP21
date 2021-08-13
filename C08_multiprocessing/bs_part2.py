from http.server import HTTPServer, BaseHTTPRequestHandler

with open('image.jpg', 'rb') as file:
    image = file.read()

class ImageLoad(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'image/jpeg')
        self.end_headers()
        self.wfile.write(image)

http_server = HTTPServer(('localhost', 8080), ImageLoad)
http_server.serve_forever()

# from http.server import HTTPServer, BaseHTTPRequestHandler
#
# with open('putty.exe', 'rb') as file:
#     app = file.read()
#
# class ImageLoad(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('content-type', 'application/octet-stream')
#         self.end_headers()
#         self.wfile.write(app)
#
# http_server = HTTPServer(('localhost', 8080), ImageLoad)
# http_server.serve_forever()