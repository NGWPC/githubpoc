from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="text/plain"):
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/hello":
            self._set_headers()
            self.wfile.write(b"world")
        else:
            self._set_headers(status_code=404)
            self.wfile.write(b"Not Found")


class SimpleServer:
    def __init__(self, host='', port=8000):
        self.host = host
        self.port = port
        self.server = HTTPServer((self.host, self.port), SimpleHTTPRequestHandler)
        self.is_running = False

    def start(self):
        print(f"Server running on {self.host}:{self.port}")
        self.is_running = True
        self.server.serve_forever()

    def stop(self):
        if self.is_running:
            self.server.shutdown()
            self.server.server_close()
            self.is_running = False


def main():
    server = SimpleServer()
    server.start()


if __name__ == "__main__":
    main()
