from tkinter import filedialog
from modelo.assistente_conversacional import AssistenteConversacional

class Controlador:
    def __init__(self, pinecone_api_key, huggingfacehub_api_key):

        # Caminho da pasta com os arquivos PDF
        self.caminho = None

        # Criando assistente conversacional
        self.assistente_conversacional = AssistenteConversacional(pinecone_api_key, huggingfacehub_api_key)

    def abrir_pasta_pdf(self) -> None:
        # Obtendo caminho das pastas
        self.caminho = filedialog.askdirectory(title="Pasta com documentos PDF")

        # Indexando arquivos PDF
        self.assistente_conversacional.indexar_documentos_pdf(self.caminho)