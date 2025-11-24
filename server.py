from http.server import SimpleHTTPRequesthandler,HTTPServer
    class Myhandler(SimpleHTTPRequesthandler):
        def do_GET(self):
            if self.path == "/":
                self.path = 'index.html'
                return super().do_GET()

            if__name__=="__main__":
        server = HTTPServer(('localhost',8000),Myhandler
        printf("Serving on htttps://localhost:8000")
        server.server_forever()
    