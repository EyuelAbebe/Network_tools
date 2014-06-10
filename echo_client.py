import socket
import sys


def client(message):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)
    client_socket.connect(('127.0.0.1', 3006))

    if isinstance(message, unicode):
        message = message.encode('utf-8')


   # message.encode('utf-8') # encode sent message
    client_socket.send(message)
    client_socket.shutdown(socket.SHUT_WR)

    buffer_size = 1024
    #done = False
    amount_received = 0
    amount_expected = len(message)
    recieved_message = ''

    while amount_received < amount_expected:
        returned_message = client_socket.recv(buffer_size) #decode whatever is received
        # #print returned_message
        # if len(recieved_message) < buffer_size:
        #     recieved_message += returned_message
        #     done = True

        recieved_message += returned_message
        amount_received += len(returned_message)
    #
    # print message
    # print recieved_message
    # assert len(message) == len(recieved_message)
    client_socket.close()

    return recieved_message #.decode('utf-8')


if __name__ == "__main__":
    print client(sys.argv[1])

