from http.server import HTTPServer, CGIHTTPRequestHandler

# CGI ハンドラの設定 
httpd = HTTPServer(('127.0.0.1', 8080), CGIHTTPRequestHandler)
httpd.serve_forever()
