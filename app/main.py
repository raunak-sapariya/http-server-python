import socket


def Request(data):
    data_str = data.decode()
    split_lines = data_str.split("\r\n")
    method, path, version = split_lines[0].split()
    return method, path, version


def main():
    server_socket = socket.create_server(("0.0.0.0", 4221))
    while True:
        client_con, add = server_socket.accept()

        with client_con:
            print("Client_Connection_Detail  -->", client_con)
            print("Client_Address_Detail -->", add)
            print(f'Connected by {add}')

            data = client_con.recv(1024)
            print("Data -->", data)


            response = b"HTTP/1.1 200 OK\r\n\r\n"
            client_con.send(response)

            method, path, version = Request(data)
            if path == "/":
                response1 = b"HTTP/1.1 200 OK\r\n\r\n"
                
            else:
                response1 = b"HTTP/1.1 404 Not Found\r\n\r\n"
            client_con.send(response1)

    server_socket.close()


if __name__ == "__main__":
    main()
