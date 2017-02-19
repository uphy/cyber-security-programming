import socket

if __name__ == '__main__':
    target_host = "localhost"
    target_port = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    client.send("Hello")
    response = client.recv(4096)

    print(response)
