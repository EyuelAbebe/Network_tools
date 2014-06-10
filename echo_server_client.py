import sys
import threading
from echo_server import Server
from echo_client import Client

def client_send_receive(message):
    _client = Client()
    _client.send(message)
    print _client.receive()


class ClientThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args)



class ServerThread(threading.Thread):
    def run(self):
        return Server().serve()

class Echo_Client_Server(threading.Thread):

    def __init__(self, _func, message):
        self.server = ServerThread().start()
        self.client = ClientThread(_func, message).start()


if __name__ == "__main__":
    _client = Echo_Client_Server(client_send_receive, sys.argv[1])

    while True:
        _new_Client = ClientThread(client_send_receive, raw_input("Give me a new input to echo: ")).start()
