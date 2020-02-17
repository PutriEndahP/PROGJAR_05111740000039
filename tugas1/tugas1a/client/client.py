import socket
import sys

HOST = 'localhost'    # server name goes in here
PORT = 31000


def put(commandName):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))
    socket1.send(commandName)
    string = commandName.split(' ', 1)
    inputFile = string[1]
    with open(inputFile, 'rb') as file_to_send:
        for data in file_to_send:
            socket1.sendall(data)
    print('PUT Successful')
    socket1.close()
    return


while(1):
    inputCommand = sys.stdin.readline().strip()
    if (inputCommand == 'quit'):
        # socket1.send('quit')
        break
    else:
        string = inputCommand.split(' ', 1)
        if (string[0] == 'put'):
            put(inputCommand)
        else:
            print ('command not found :(')