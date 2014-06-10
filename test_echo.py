import pytest

from echo_client import client
import echo_server

def test_echo():

    client_message = client("Hi there")
    assert client_message == "Hi there"

    client_message = client("Στο παρελθόν έχει χρησιμοποιηθεί και για άλλες γλώσσες")
    assert client_message == "Στο παρελθόν έχει χρησιμοποιηθεί και για άλλες γλώσσες"

    client_message = client("Արդի ժամանակներում գիտության մեջ գերակշռում է")
    assert client_message == "Արդի ժամանակներում գիտության մեջ գերակշռում է"
