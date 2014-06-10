import pytest

from echo_client import Client
from echo_server import Server

def test_echo():

    _server = Server().serve()

    _client = Client()
    _client.send("Hi there")
    assert _client.receive() == "Hi there"

    _client = Client()
    _client.send(u"Στο παρελθόν έχει χρησιμοποιηθεί και για άλλες γλώσσες")
    assert _client.receive() == u"Στο παρελθόν έχει χρησιμοποιηθεί και για άλλες γλώσσες"

    _client = Client()
    _client.send(u"臍帯血に含まれる造血幹細胞移植は骨髄移植や末梢血幹細胞移植と並ぶ造血細胞の移植術であるが、臍帯血は骨髄や動員末梢血幹細胞に比べると造血幹細胞の数が少なく、生着率が悪かったり造血の回復が遅いデメリット(移植初期の失敗が多い)はあるが、適切に保存された臍帯血は短期間で移植が可能で、造血幹細胞が一旦生着し安定した造血が始まると骨髄や動員末梢血幹細胞による造血よりも")
    assert _client.receive() == u"臍帯血に含まれる造血幹細胞移植は骨髄移植や末梢血幹細胞移植と並ぶ造血細胞の移植術であるが、臍帯血は骨髄や動員末梢血幹細胞に比べると造血幹細胞の数が少なく、生着率が悪かったり造血の回復が遅いデメリット(移植初期の失敗が多い)はあるが、適切に保存された臍帯血は短期間で移植が可能で、造血幹細胞が一旦生着し安定した造血が始まると骨髄や動員末梢血幹細胞による造血よりも"
