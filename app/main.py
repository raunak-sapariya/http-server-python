import socket

class Request(object):
    def __init__(self, data) -> None:
        data_str = data.decode()
        lines = data_str.split("\r\n")
        method, path, version = lines[0].split()
        self.method = method
        self.path = path
        self.version = version

def main():
    
    server_socket = socket.create_server(("0.0.0.0", 4221))
    while True:
        conn, addr = server_socket.accept()  
        with conn:
            print("Connected by", addr)
            data = conn.recv(1024)
            print(data)
            resp = "HTTP/1.1 200 OK\r\n\r\n".encode()
            conn.send(resp)
        try:
            conn, addr = server_socket.accept()  
            with conn:
                print("Connected by", addr)
                data = conn.recv(1024)
                print("data: %s" % data)
                req = Request(data)
                if req.path == "/":
                    resp = "HTTP/1.1 200 OK\r\n\r\n"
                else:
                    resp = "HTTP/1.1 404 Not Found\r\n\r\n"
                conn.send(resp.encode())
        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()
