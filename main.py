from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from pinecone import Pinecone

class AssistenteConversacional:
    def __init__(self, pinecone_api_key, huggingfacehub_api_key):
        self.__inicializar_modelo_pretreinado(huggingfacehub_api_key)
        self.__inicializar_pinecone(pinecone_api_key)

    def __inicializar_modelo_pretreinado(self, huggingfacehub_api_key):
        model_name = "Qwen/Qwen2.5-1.5B"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
        self.chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

    def __inicializar_pinecone(self, pinecone_api_key):
        self.pinecone = Pinecone(pinecone_api_key)
