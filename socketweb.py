#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 6553         # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # conn.sendall(b'blabla')
        while True:
            data = conn.recv(1024)
            print(data)
            if not data: break
            conn.sendall(b'lslsl')
            conn.close() 
            # if not data:
            #     break
            # conn.sendall( b'mongolian keyboard yum shvv dee ho2 ho2 ho2 ho2 ho2 ho2 ho2')

# OSError Bad file descriptor