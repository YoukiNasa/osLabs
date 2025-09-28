# socket_demo.py - 单文件Socket演示
import socket

def simple_server():
    s = socket.socket()
    s.bind(('localhost', 8888))
    s.listen(1)
    print("waiting connecting...")
    
    client, addr = s.accept()
    print(f"Client {addr} Connected!")
    
    while True:
        msg = client.recv(1024).decode()
        if not msg or msg == 'quit':
            break
        print(f"received: {msg}")
        client.send(f"echo: {msg}".encode())

    client.close()
    s.close()

def simple_client():
    s = socket.socket()
    s.connect(('localhost', 8888))
    print("Connected successfully! Please enter your message:")
    
    while True:
        msg = input("> ")
        s.send(msg.encode())
        if msg == 'quit':
            break
        response = s.recv(1024).decode()
        print(f"server: {response}")
    
    s.close()

if __name__ == "__main__":
    choice = input("Start server(s) or client(c)? ").lower()
    
    if choice == 's':
        simple_server()
    elif choice == 'c':
        simple_client()
    else:
        print("Invalid choice")