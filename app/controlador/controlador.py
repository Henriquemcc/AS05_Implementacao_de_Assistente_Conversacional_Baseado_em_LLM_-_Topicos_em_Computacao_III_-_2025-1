from tkinter import filedialog
from modelo.assistente_conversacional import AssistenteConversacional
from visao.janela_principal import JanelaPrincipal

class Controlador:
    def __init__(self, pinecone_api_key, huggingfacehub_api_key):

        # Caminho da pasta com os arquivos PDF
        self.caminho = None

        # Criando assistente conversacional
        self.assistente_conversacional = AssistenteConversacional(pinecone_api_key, huggingfacehub_api_key)

        # Criando janela principal
        self.janela_principal = JanelaPrincipal(self)

    def abrir_pasta_pdf(self) -> None:
        # Obtendo caminho das pastas
        self.caminho = filedialog.askdirectory(title="Pasta com documentos PDF")

        # Indexando arquivos PDF
        self.assistente_conversacional.indexar_documentos_pdf(self.caminho)

    def enviar_mensagem(self):
        pass