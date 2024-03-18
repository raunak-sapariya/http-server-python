import socket




def main():
    
    print("----------------------------------------")

    server_socket = socket.create_server(("localhost", 4221))
    
    try:
        while True:
            client_con,add=server_socket.accept()
            print(f'Connected to {add}')
            response=b"HTTP/1.1 200 OK\r\n\r\n"
            client_con.sendall(response)

    except ConnectionError:
        print(ConnectionError)
    finally :
        print("closing")
        server_socket.close()




   

    print("TCP CONNECTION")
    # con.close()

if __name__ == "__main__":
    main()
