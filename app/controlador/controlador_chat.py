class ControladorChat:
    def __init__(self, pai):
        # Guardando o pai
        self.pai = pai

        # Array que armazena o histórico de mensagens trocadas
        self.mensagens = []
