#!/usr/bin/env python
try:
    # Python 3
    from http.server import HTTPServer, SimpleHTTPRequestHandler, test as test_orig
    import sys
    def test (*args):
        test_orig(*args, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
except ImportError: # Python 2
    from BaseHTTPServer import HTTPServer, test
    from SimpleHTTPServer import SimpleHTTPRequestHandler





class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Content-Encoding', 'gzip')
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer)


# Some additional context on this server / gzip compression:
# https://stackoverflow.com/questions/21956683/enable-access-control-on-simple-http-server
# https://stackoverflow.com/questions/9622998/how-to-use-content-encoding-gzip-with-python-simplehttpserver
# https://www.afternerd.com/blog/python-http-server/
# https://en.wikipedia.org/wiki/HTTP_compression
