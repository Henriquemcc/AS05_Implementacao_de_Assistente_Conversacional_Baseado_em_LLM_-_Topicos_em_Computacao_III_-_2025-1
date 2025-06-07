from controlador.controlador import Controlador

# Chaves de API
pinecone_api_key = ""
huggingfacehub_api_key = ""

if __name__ == '__main__':
    controlador = Controlador(pinecone_api_key, huggingfacehub_api_key)