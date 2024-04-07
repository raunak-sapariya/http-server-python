import socket

def Request(data):
        data_str = data.decode()
        lines = data_str.split("\r\n")
        method, path, version = lines[0].split()
        return data_str,lines,method

def main():
    server_socket = socket.create_server(("0.0.0.0", 4221))
    while True:
        client_conn, addr = server_socket.accept()
        with client_conn:
            print("Connected by", addr)
            data = client_conn.recv(1024)
            print(data)
            req = Request(data)
            if req[1] == "/":
                response = "HTTP/1.1 200 OK\r\n\r\nHello, World!"
            else:
                response = "HTTP/1.1 404 Not Found\r\n\r\nPage Not Found"
            client_conn.send(response.encode())

if __name__ == "__main__":
    main()
