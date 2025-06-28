from controlador.controlador import Controlador
import nltk
from dotenv import load_dotenv

# Chaves de API
load_dotenv()
pinecone_api_key = os.getenv("PINECONE_API_KEY")
huggingfacehub_api_key = os.getenv("HUGGINGFACEHUB_API_KEY")

if __name__ == '__main__':
    # Baixando o Tokenizer
    nltk.download('punkt_tab')

    # Executando programa
    controlador = Controlador(pinecone_api_key, huggingfacehub_api_key)
    controlador.janela_principal.mainloop()