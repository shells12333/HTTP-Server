import sys
from file_handler import handle_file_request

def parseRequest(req):
    ok_default = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
    not_found = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n"

    req = req.decode('utf-8')
    lines = req.splitlines()
    if not lines:
        return not_found.encode()

    req_line = lines[0]
    method, path, http_version = req_line.split()

    if method == "POST":
        return handle_file_request(req, path)

    if path == "/":
        return ok_default.encode()
    
    # Handle echo and user-agent logic here
    # For example:
    if path.startswith("/echo/"):
        body = path.split("/echo/", 1)[1]
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(body)}\r\n"
            "\r\n"
            f"{body}"
        ).encode()
        return response
    
    elif path.startswith("/user-agent"):
        user_agent = ""
        for line in lines[1:]:
            if line.startswith("User-Agent:"):
                user_agent = line.split(": ", 1)[1]
                break
        
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(user_agent)}\r\n"
            "\r\n"
            f"{user_agent}"
        ).encode()
        return response
    
    return not_found.encode()