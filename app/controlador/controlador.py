import datetime
from tkinter import filedialog
from modelo.assistente_conversacional import AssistenteConversacional
from visao.janela_principal import JanelaPrincipal
from modelo.mensagem import Mensagem

class Controlador:
    def __init__(self, pinecone_api_key, huggingfacehub_api_key):

        # Caminho da pasta com os arquivos PDF
        self.caminho = None

        # Contador das mensagens
        self.contador_mensagens = 0

        # Criando assistente conversacional
        self.assistente_conversacional = AssistenteConversacional(pinecone_api_key, huggingfacehub_api_key)

        # Criando janela principal
        self.janela_principal = JanelaPrincipal(self)

    def abrir_pasta_pdf(self) -> None:
        # Obtendo caminho das pastas
        self.caminho = filedialog.askdirectory(title="Pasta com documentos PDF")

        # Exibindo cursor de relógio
        self.janela_principal.set_cursor("watch")

        # Indexando arquivos PDF
        self.assistente_conversacional.indexar_documentos_pdf(self.caminho)

        # Exibindo cursor padrão
        self.janela_principal.set_cursor("")

    def enviar_mensagem(self, mensagem: str, f):
        # Obtendo resposta
        resposta = self.assistente_conversacional.perguntar(mensagem)

        # Convertendo mensagem para uma instância de Mensagem
        mensagem = Mensagem(self.contador_mensagens, "Você", datetime.datetime.now(), mensagem)
        self.contador_mensagens+=1

        # Convertendo resposta para uma instância de Mensagem
        resposta = Mensagem(self.contador_mensagens, "Assistente Conversacional", datetime.datetime.now(), resposta)
        self.contador_mensagens += 1

        # Retornando mensagem e resposta para a função de callback
        f([mensagem, resposta])
