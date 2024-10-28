from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Mock data (replace this with actual PostgreSQL queries in production)
TERMINALS = [
    {"id": 1, "name": "Terminal A", "location": "North Wing", "status": "active"},
    {"id": 2, "name": "Terminal B", "location": "South Wing", "status": "active"},
    {"id": 3, "name": "Terminal C", "location": "East Wing", "status": "maintenance"}
]

class TerminalService(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/terminals':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = json.dumps({
                "status": "success",
                "data": TERMINALS
            })
            
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"status": "error", "message": "Not found"}')

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, TerminalService)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()