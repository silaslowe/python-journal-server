import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from sqlite3.dbapi2 import PARSE_DECLTYPES

from entries import get_all_entries, get_single_entry,delete_entry, get_all_searched_entries, create_entry
from moods import get_all_moods

class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'keyword'
            value = pair[1]  # 'react'

            return ( resource, key, value )

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        
        response = {} 

        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            (resource, id) = parsed
            
            if resource == "moods":
                response = f"{get_all_moods()}"

            elif resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"

                else:
                    response = f"{get_all_entries()}"
        
        elif len(parsed) == 3:
            (resource, key, value) = parsed

            if key == "search_term" and resource == "entries":
                response = get_all_searched_entries(value)

        self.wfile.write(response.encode())
    
    def do_DELETE(self):
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            delete_entry(id)

        self.wfile.write("".encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_entry = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "entries":
            new_entry = create_entry(post_body)

        self.wfile.write(f"{new_entry}".encode())
        
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()        