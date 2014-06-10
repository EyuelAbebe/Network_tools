import socket

def _socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    server_socket.bind(('127.0.0.1', 3006))

    while True:
        server_socket.listen(1)

        buffer_size = 1024
        conn, client_address = server_socket.accept()

        response = ''
        done = False
        while not done:
            recieved_message = conn.recv(buffer_size)
            print recieved_message
            if len(recieved_message) < buffer_size:
                response += recieved_message
                done = True

            response += recieved_message

        print response
        conn.sendall(response)
        conn.shutdown(socket.SHUT_WR)


if __name__ == "__main__":
    _socket()
