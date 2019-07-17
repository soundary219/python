import socket
def main():
    host = '127.0.0.1'
    port = 5000
    #create socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Created socket')
    #bind host and port
    s.connect((host,port))
    print("connected to the server..")

    message=input("enter the message to send to the server:\n")
    print("enter q to quit sending message")
    while message != 'q':
        s.send(str.encode(message,('utf-8')))
        data = s.recv(1024).decode('utf-8')
        print("data received from server :{}".format(data))
        message=input("enter message to send to server:\n")
        print(message)
    s.close()

if __name__=='__main__':
    main()
