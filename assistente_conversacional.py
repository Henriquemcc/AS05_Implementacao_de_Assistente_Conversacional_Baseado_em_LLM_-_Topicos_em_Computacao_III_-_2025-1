from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from pinecone import Pinecone
from utils import gerar_random_string
from PyPDF2 import PdfReader
import time
import os


def ler_texto_pdf(caminho: str) -> str:
    pdf_reader = PdfReader(caminho)
    texto = ""
    for pagina in pdf_reader.pages:
        texto += pagina.extract_text() + "\n"
    return texto

class AssistenteConversacional:
    def __init__(self, pinecone_api_key, huggingfacehub_api_key):
        self.pinecone_index_name_space = gerar_random_string()
        self.pinecone_index = None
        self.pinecone_index_name = "as05-topicos3"
        self.pinecone_top_k = 3
        self.__inicializar_modelo_pretreinado(huggingfacehub_api_key)
        self.__inicializar_pinecone(pinecone_api_key)

    def __del__(self):
        # Apagando namespace
        self.pinecone.delete(delete_all=True, namespace=self.pinecone_index_name_space)

    def __inicializar_modelo_pretreinado(self, huggingfacehub_api_key):
        login(huggingfacehub_api_key)
        model_name = "distilbert-base-uncased-distilled-squad"
        self.chatbot = pipeline("question-answering", model=model_name)

    def __inicializar_pinecone(self, pinecone_api_key):
        self.pinecone = Pinecone(pinecone_api_key)

    def indexar_documentos(self, documentos):
        if self.pinecone_index is None:
            self.pinecone_index = self.pinecone.Index(self.pinecone_index_name)
        self.pinecone_index.upsert_records(
            namespace=self.pinecone_index_name_space,
            records=documentos
        )
        time.sleep(60)

    def indexar_documentos_pdf(self, pasta: str):
        for arquivo in os.listdir(pasta):
            if arquivo.lower().endswith(".pdf"):
                caminho_pdf = os.path.join(pasta, arquivo)
                texto = ler_texto_pdf(caminho_pdf)
                self.indexar_documentos([{
                    "id": arquivo,
                    "text": texto
                }])

    def perguntar(self, pergunta):
        # Obtendo os resultados do Pinecone
        resultados_pinecone = self.pinecone_index.search(
            namespace = self.pinecone_index_name_space,
            query = {
                "inputs": {"text": pergunta},
                "top_k": self.pinecone_top_k
            }
        )

        # Convertendo resultados
        resultados = []
        for resultado in resultados_pinecone['result']['hits']:
            resultados.append(resultado['fields']['text'])
        resultados = " ".join(resultados)

        # Fazendo o ChatBot responder
        resposta =  self.chatbot(
            {'question': pergunta,
             'context': resultados
        })

        return resposta['answer']