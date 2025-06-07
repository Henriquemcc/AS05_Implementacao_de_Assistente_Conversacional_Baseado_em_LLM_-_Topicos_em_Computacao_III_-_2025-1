from controlador.controlador import Controlador

# Chaves de API
pinecone_api_key = "pcsk_5k26G8_PPWJijDSULaGXtVLyycFu8vGeiFNxocFGsSijhyMwxUrm1pg8kj5CZF7a21QfWG"
huggingfacehub_api_key = "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"

if __name__ == '__main__':
    controlador = Controlador(pinecone_api_key, huggingfacehub_api_key)
    controlador.janela_principal.mainloop()