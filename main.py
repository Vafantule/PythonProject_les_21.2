from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "localhost"
PORT = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/css/styles.css":
            try:
                with open("css/styles.css", encoding="utf-8") as file:
                    css_content = file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/css; charset=utf-8")
                self.end_headers()
                self.wfile.write(css_content.encode("utf-8"))
            except Exception:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Not Found")
        else:
            try:
                with open("contacts.html", encoding="utf-8") as file:
                    html_content = file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html_content.encode("utf-8"))
            except Exception:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Internal Server Error")

if __name__ == "__main__":
    webServer = HTTPServer((HOST, PORT), MyServer)
    print(f"Server started http://{HOST}:{PORT}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
