from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/set_cookie':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
         
            self.send_header('Set-Cookie', 'my_cookie=cookie_value')
            self.end_headers()
            self.wfile.write(b'Cookie is set!')
        
        elif self.path == '/get_cookie':
         
            cookie_header = self.headers.get('Cookie')
            if cookie_header:
                cookie_value = cookie_header.split('=')[1]
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                response = f'The value of the cookie is: {cookie_value}'
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                response = 'No cookie found'
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server started on port 8000...")
    httpd.serve_forever()
