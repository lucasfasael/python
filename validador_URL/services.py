import db
import requests


def create(url):
    db.create(url)


def remove(url):
    db.remove(url)


def update(url):
    print("Batata Update")


def findAll():
    return db.findAll()


def validatorURL(url):
    try:
        # Faz uma solicitação GET à URL usando a biblioteca requests
        response = requests.get(url)
        if response.status_code == 200:

            return True  # Exibe uma mensagem informando que a URL está ativa
        else:

            return False
            # Exibe uma mensagem informando o código de status retornado pela URL
    except requests.exceptions.RequestException:
        return False
