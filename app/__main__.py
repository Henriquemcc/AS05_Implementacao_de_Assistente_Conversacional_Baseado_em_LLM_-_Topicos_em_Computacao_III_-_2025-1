from visao.janela_principal import JanelaPrincipal

# Chaves de API
pinecone_api_key = ""
huggingfacehub_api_key = ""

if __name__ == '__main__':
    janela_principal = JanelaPrincipal(pinecone_api_key, huggingfacehub_api_key)
    janela_principal.mainloop()