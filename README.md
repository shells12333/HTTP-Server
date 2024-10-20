# Basic HTTP Server

Developed to understand socket programming, multithreading, and the HTTP protocol.

## Functionality
POST /files/<filename>: Create or update a file with the request body.
GET /files/<filename>: Retrieve the contents of a file.
GET /echo/<message>: Echo back the message.
GET /user-agent: Return the User-Agent from the request headers.

## Usage

Run the server with the base directory as an argument:
```bash
python server.py <base_directory>