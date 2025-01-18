import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        names = query.get('name', [])

        # Sample marks data
        marks_data = {
            "X": 10,
            "Y": 20,
            "Z": 30  # Add more sample data as needed
        }

        # Get the marks for the requested names
        marks = [marks_data.get(name, 0) for name in names]

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"marks": marks}).encode('utf-8'))
        return
