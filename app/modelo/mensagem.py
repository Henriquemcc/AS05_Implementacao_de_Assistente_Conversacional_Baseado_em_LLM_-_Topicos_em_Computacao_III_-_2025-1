import datetime

class Mensagem:
    def __init__(self, indice: int, autor: str, data: datetime.datetime, conteudo: str):
        self.indice = indice
        self.autor = autor
        self.data = data
        self.conteudo = conteudo

    def __str__(self) -> str:
        return "[{}] {}: {}".format(self.data.strftime("%Y-%m-%d %H:%M:%S"), self.autor, self.conteudo)