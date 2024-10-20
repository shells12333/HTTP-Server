import socket
import threading
import sys
from request_handler import parseRequest

def handleClient(conn, addr):
    data = conn.recv(1024)
    response = parseRequest(data)
    print(response.decode('utf-8'))
    conn.sendall(response)
    conn.close()

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    all_threads = []

    try:
        while True:
            conn, addr = server_socket.accept()
            print("Client connected:", addr)
            t = threading.Thread(target=handleClient, args=(conn, addr))
            t.start()
            all_threads.append(t)
    except KeyboardInterrupt:
        print("Shutting down server.")
    finally:
        server_socket.close()
        for t in all_threads:
            t.join()

if __name__ == "__main__":
    main()