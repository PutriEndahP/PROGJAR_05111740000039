import socket

TARGET_IP = "172.17.249.97"
TARGET_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes('Putri Endah'.encode()),(TARGET_IP,TARGET_PORT))