import os
import random
import string
import time

import nltk
from PyPDF2 import PdfReader
from huggingface_hub import login
from pinecone import Pinecone
from transformers import pipeline


def gerar_random_string(length = 10) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def ler_texto_pdf(caminho: str) -> str:
    pdf_reader = PdfReader(caminho)
    texto = ""
    for pagina in pdf_reader.pages:
        texto += pagina.extract_text() + "\n"
    return texto

def dividir_em_chunks_semantic(texto, tamanho_max=500):
    sentencas = nltk.tokenize.sent_tokenize(texto)
    chunks = []
    atual = ""
    for s in sentencas:
        if len(atual.split()) + len(s.split()) <= tamanho_max:
            atual += " " + s
        else:
            chunks.append(atual.strip())
            atual = s
    if atual:
        chunks.append(atual.strip())
    return chunks

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
        self.pinecone_index.delete(delete_all=True, namespace=self.pinecone_index_name_space)

    def __inicializar_modelo_pretreinado(self, huggingfacehub_api_key):
        login(huggingfacehub_api_key)
        model_name = "deepset/roberta-base-squad2"
        self.chatbot = pipeline("question-answering", model=model_name)

    def __inicializar_pinecone(self, pinecone_api_key):
        self.pinecone = Pinecone(pinecone_api_key)

    def indexar_documentos(self, documentos, delay: bool = True):
        if self.pinecone_index is None:
            self.pinecone_index = self.pinecone.Index(self.pinecone_index_name)
        self.pinecone_index.upsert_records(
            namespace=self.pinecone_index_name_space,
            records=documentos
        )
        if delay:
            time.sleep(60)

    def indexar_documentos_pdf(self, pasta: str):
        for arquivo in os.listdir(pasta):
            if arquivo.lower().endswith(".pdf"):
                caminho_pdf = os.path.join(pasta, arquivo)
                texto = ler_texto_pdf(caminho_pdf)
                chunks = dividir_em_chunks_semantic(texto)
                for index, chunk in enumerate(chunks):
                    self.indexar_documentos([{
                        "id": "{}-{}".format(arquivo, index),
                        "text": chunk
                    }], delay=False)

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
        print("Resultados:\n{}".format(str(resultados)))

        # Fazendo o ChatBot responder
        melhor_resposta = None
        maior_score = 0
        for contexto in resultados:
            resposta = self.chatbot(question=pergunta, context=contexto)
            if resposta['score'] > maior_score:
                maior_score = resposta['score']
                melhor_resposta = resposta['answer']
        return melhor_resposta