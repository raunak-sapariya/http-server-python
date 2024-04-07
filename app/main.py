import socket

def Request(data):
        data_str = data.decode()
        lines = data_str.split("\r\n")
        method, path, version = lines[0].split()
        return method,path,version

def main():
    server_socket = socket.create_server(("0.0.0.0", 4221))
    while True:
        client_conn, addr = server_socket.accept()
        with client_conn:
            print("Connected by", addr)

            data = client_conn.recv(1024)
            print(data)


            response = b"HTTP/1.1 200 OK\r\n\r\n"
            client_conn.send(response)

            req = Request(data)
            print(req)
            if req[1] == "/":
                client_conn.send(b"HTTP/1.1 200 OK\r\n\r\nHello, World!")
            else:
                client_conn.send(b"HTTP/1.1 404 Not Found\r\n\r\nPage Not Found")
            

if __name__ == "__main__":
    main()
