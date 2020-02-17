import socket
import sys

HOST = 'localhost'    # server name goes in here
PORT = 31000

def get(commandName):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))
    socket1.send(commandName)
    string = commandName.split(' ', 1)
    inputFile = string[1]
    with open(inputFile, 'wb') as file_to_write:
        while True:
            data = socket1.recv(1024)
            # print data
            if not data:
                break
            # print data
            file_to_write.write(data)
    file_to_write.close()
    print ('GET Successful')
    socket1.close()
    return


while(1):
    inputCommand = sys.stdin.readline().strip()
    if (inputCommand == 'quit'):
        # socket.send('quit')
        break
    else:
        string = inputCommand.split(' ', 1)
        if (string[0] == 'get'):
            get(inputCommand)
        else:
            print ('command not found :(')