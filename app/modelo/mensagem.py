import datetime

class Mensagem:
    def __init__(self, autor: str, data: datetime.datetime, conteudo: str):
        self.autor = autor
        self.data = data
        self.conteudo = conteudo
