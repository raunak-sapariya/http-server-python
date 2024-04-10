import socket
import threading
from concurrent.futures import ThreadPoolExecutor



def Request(data):

    data_str = data.decode()
    lines = data_str.split("\r\n")
    method, path, version = lines[0].split()
    header={}
    for line in lines:
        if ":" in line:
            key,value=line.split(": ")
            header[key]=value

    return method, path,version,header,lines

def handle_conn(client_conn,addr):
    try:
        with client_conn:
            print("Connected by", addr)
            

            data = client_conn.recv(1024)
            print(data)
            
            req = Request(data)
            print("---------------------",req)
           

            if req[1] == "/":
                accept_encoding = req[3].get("Accept-Encoding", "")
                host=req[3]["Host"]
                user_agent=req[3]["User-Agent"]
                content= "HELLO WORLD!"
                response = "\r\n".join(["HTTP/1.1 200 OK",
                            "Content-Type: text/plain",
                            f"Content-Length: {len(content)}",
                            f"Host: {host}",
                            f'User-Agent: {user_agent}',
                            f"Accept-Encoding: {accept_encoding}",
                            "",
                            content,
                ]).encode() 
                client_conn.sendall(response)
            


            elif req[1].startswith("/echo/") :
                content= req[1][6:]
                accept_encoding=req[3]["Accept-Encoding"]
                host=req[3]["Host"]
                user_agent=req[3]["User-Agent"]
                response = "\r\n".join(["HTTP/1.1 200 OK",
                            "Content-Type: text/plain",
                            f"Content-Length: {len(content)}",
                            f"Host: {host}",
                            f'User-Agent: {user_agent}',
                            f"Accept-Encoding: {accept_encoding}",
                            "",
                            content,
                ]).encode() 
                client_conn.sendall(response)
            

            elif req[1].startswith("/user-agent") :
                user_agent=req[3]["User-Agent"]
                accept_encoding=req[3]["Accept-Encoding"]
                host=req[3]["Host"]
                response = "\r\n".join(["HTTP/1.1 200 OK",
                            "Content-Type: text/plain",
                            f"Content-Length: {len(user_agent)}",
                            f"Host: {host}",
                            f'User-Agent: {user_agent}'
                            f"Accept-Encoding: {accept_encoding}",
                            "",
                            user_agent,
                ]).encode() 
                client_conn.sendall(response)


            else:
                 accept_encoding = req[3]["Accept-Encoding"]
                 host = req[3]["Host"]
                 content="Page Not Found"
                 user_agent=req[3]["User-Agent"]
                 response = "\r\n".join(["HTTP/1.1 404 Not Found",
                                        "Content-Type: text/plain",
                                        f"Content-Length: {len(content)}",
                                        f"Host: {host}",
                                        f'User-Agent: {user_agent}',
                                        f"Accept-Encoding: {accept_encoding}",
                                        "",
                                        content,
                 ]).encode()
                 client_conn.sendall(response)
    except Exception as e:
        print(f"Error handling connection: {e}")
    finally:
        client_conn.close()    

def main():
    server_socket = socket.create_server(("0.0.0.0", 4221))
    thread_pool = ThreadPoolExecutor(max_workers=5)

    while True:
        client_conn, addr = server_socket.accept()
        thread_pool.submit(handle_conn, client_conn, addr)

       
        
        


if __name__ == "__main__":
    main()