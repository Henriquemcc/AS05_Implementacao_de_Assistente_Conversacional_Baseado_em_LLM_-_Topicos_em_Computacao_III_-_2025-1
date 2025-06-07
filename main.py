import string

from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from pinecone import Pinecone
import random


def gerar_random_string(length = 10) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class AssistenteConversacional:
    def __init__(self, pinecone_api_key, huggingfacehub_api_key):
        self.pinecone_index = None
        self.pinecone_index_name = "indice_assistente_conversacional"
        self.pinecone_index_name_space = None
        self.pinecone_top_k = 3
        self.__inicializar_modelo_pretreinado(huggingfacehub_api_key)
        self.__inicializar_pinecone(pinecone_api_key)

    def __inicializar_modelo_pretreinado(self, huggingfacehub_api_key):
        login(huggingfacehub_api_key)
        model_name = "Qwen/Qwen2.5-1.5B"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
        self.chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

    def __inicializar_pinecone(self, pinecone_api_key):
        self.pinecone = Pinecone(pinecone_api_key)

    def indexar_documentos(self, documentos):
        self.pinecone_index_name_space = gerar_random_string()
        if self.pinecone_index is None:
            self.pinecone_index = self.pinecone.Index(self.pinecone_index_name)
        self.pinecone_index.upsert_records(
            namespace=self.pinecone_index_name_space,
            records=documentos
        )