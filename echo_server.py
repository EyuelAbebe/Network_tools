import socket

class Server():

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
        self.server_socket.bind(('127.0.0.1', 3010))

    def serve(self):

        while True:
            self.server_socket.listen(1)

            buffer_size = 32
            conn, client_address = self.server_socket.accept()

            response = []
            done = False
            while not done:
                recieved_message = conn.recv(buffer_size)
                print recieved_message
                if not recieved_message:
                    done = True

                response.append(recieved_message)


            response = ''.join(response)
            print response
            conn.sendall(response)
            conn.shutdown(socket.SHUT_WR)


if __name__ == "__main__":
    server = Server().serve()
