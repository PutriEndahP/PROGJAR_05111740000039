import socket
import sys

HOST = 'localhost'
PORT = 31000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))

socket.listen(1)
while (1):
    conn, addr = socket.accept()
    print ('New client connected ..')
    reqCommand = conn.recv(1024)
    print ('Client> %s' %(reqCommand))
    if (reqCommand == 'quit'):
        break
    else:
        string = reqCommand.split(' ', 1) 
        reqFile = string[1]

        if (string[0] == 'get'):
            with open(reqFile, 'rb') as file_to_send:
                for data in file_to_send:
                    conn.sendall(data)
            print ('Send Successful')
        else:
            print ('command not found :(')
    conn.close()

socket.close()