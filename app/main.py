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

    return method, path,version,header,lines

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
           

            if req[1] == "/":
                accept_encoding=req[3]["Accept-Encoding"]
                host=req[3]["Host"]
                response = "\r\n".join(["HTTP/1.1 200 OK",
                            "Content-Type: text/plain",
                            f"Content-Length: 0",
                            f"Host: {host}",
                            f"Accept-Encoding: {accept_encoding}",
                            "",
                            "HELLO WORLD!",
                ]).encode() 
                client_conn.send(response)


            elif req[1].startswith("/echo/"):
                content= req[1][6:]
                accept_encoding=req[3]["Accept-Encoding"]
                host=req[3]["Host"]
                response = "\r\n".join(["HTTP/1.1 200 OK",
                            "Content-Type: text/plain",
                            f"Content-Length: {len(content)}",
                            f"Host: {host}",
                            f"Accept-Encoding: {accept_encoding}",
                            "",
                            content,
                ]).encode() 
                client_conn.send(response)
            

            elif "User-Agent" in req[3]:
                user_agent=req[3]["User-Agent"]
                accept_encoding=req[3]["Accept-Encoding"]
                host=req[3]["Host"]
                response = "\r\n".join(["HTTP/1.1 200 OK",
                            "Content-Type: text/plain",
                            f"Content-Length: {len(user_agent)}",
                            f"Host: {host}",
                            f"Accept-Encoding: {accept_encoding}",
                            "",
                            user_agent,
                ]).encode() 
                client_conn.send(response)


            else:
                 accept_encoding = req[3]["Accept-Encoding"]
                 host = req[3]["Host"]
                 response = "\r\n".join(["HTTP/1.1 404 Not Found",
                                        "Content-Type: text/plain",
                                        f"Content-Length: 0",
                                        f"Host: {host}",
                                        f"Accept-Encoding: {accept_encoding}",
                                        "",
                                        "Page Not Found",
                 ]).encode()
                 client_conn.send(response)



if __name__ == "__main__":
    main()