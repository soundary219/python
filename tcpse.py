#server side
import socket
def main():
    host = '127.0.0.1'#local host
    port = 5000
    #Create socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Created socket")
    #bind host anf port to socket
    s.bind((host,port))
    print("binded host and port to socket")
    #listen one connection at a time
    s.listen(1)
    #accept connection
    print("Waiting for client to connect..")
    conn,addr = s.accept()
    print("connection from:"+str(addr))
    #server runs infinitely for send and recv msg
    while True:
        #receive 1024 bytes of data from client at a time
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(data)
        data = data.upper()
        print("sending :"+data)
        conn.send(data.encode('utf-8'))

    conn.close()
    
if __name__ =='__main__':
    main()


