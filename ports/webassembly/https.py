from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl, os
#os.system("openssl req -nodes -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -subj '/CN=mylocalhost'")
port = 443

# https://gist.github.com/pezcode/d51926bdbadcbd4f22f5a5d2fb8e0394
class Handler(SimpleHTTPRequestHandler):
    extensions_map = {
        '': 'application/octet-stream',
        '.css':	'text/css',
        '.html': 'text/html',
        '.jpg': 'image/jpg',
        '.js':	'application/x-javascript',
        '.json': 'application/json',
        '.manifest': 'text/cache-manifest',
        '.png': 'image/png',
        '.wasm':	'application/wasm',
        '.xml': 'application/xml',
        '.mjs': 'text/javascript',
        '.map': 'text/plain',
    }

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        SimpleHTTPRequestHandler.end_headers(self)

httpd = HTTPServer(('0.0.0.0', port), Handler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile="cert.pem", server_side=True)
print(f"Server running on https://0.0.0.0:{port}")
httpd.serve_forever()