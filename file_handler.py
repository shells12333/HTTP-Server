import sys

def handle_file_request(req, path):
    ok_created = "HTTP/1.1 201 Created\r\n\r\n"
    not_found = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n"

    lines = req.split('\r\n')
    empty_line = lines.index("") + 1
    body = '\r\n'.join(lines[empty_line:])
    base_dir = sys.argv[1]  # Updated to read from command-line argument
    filename = path[7:]  # Extract filename from path

    if path.startswith("/files"):
        try:
            with open(f"{base_dir}/{filename}", "w") as f:
                f.write(body)
                return ok_created.encode()
        except Exception:
            return not_found.encode()
    else:
        # Handle GET requests for files
        try:
            with open(f"{base_dir}/{filename}", "r") as f:
                body = f.read()
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: application/octet-stream\r\n"
                f"Content-Length: {len(body)}\r\n"
                "\r\n"
                f"{body}"
            ).encode()
            return response
        except Exception:
            return not_found.encode()