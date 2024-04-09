import socket

def Request(data):
    data_str = data.decode()
    lines = data_str.split("\r\n")[:]
    method, path, version = lines[0].split()
    header={}
    for line in lines:
        if ":" in line:
            key,value=line.split(": ")
            header[key]=value

    return method, path,version,lines,header

def main():
    server_socket = socket.create_server(("0.0.0.0", 4221))
    while True:
        client_conn, addr = server_socket.accept()
        with client_conn:
            print("Connected by", addr)

            data = client_conn.recv(1024)
            print(data)
            
            req = Request(data)
            print(req)
            print("----------------------------------------------------------",req[3])

            if req[1] == "/":
                client_conn.send(b"HTTP/1.1 200 OK\r\n\r\nHello, World!")



            elif req[1].startswith("/echo/"):
                content= req[1][6:]
                response = "\r\n".join(["HTTP/1.1 200 OK",
                            "Content-Type: text/plain",
                            f"Content-Length: {len(content)}",
                            "",
                            content,
                ])
                client_conn.send(response)
            


            else:
                client_conn.send(b"HTTP/1.1 404 Not Found\r\n\r\nPage Not Found")



if __name__ == "__main__":
    main()