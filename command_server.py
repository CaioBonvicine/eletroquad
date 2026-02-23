import socket

def wait_for_command():
    HOST = '0.0.0.0'
    PORT = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Aguardando comando...")

    conn, addr = server.accept()
    data = conn.recv(1024).decode()

    conn.close()
    return data