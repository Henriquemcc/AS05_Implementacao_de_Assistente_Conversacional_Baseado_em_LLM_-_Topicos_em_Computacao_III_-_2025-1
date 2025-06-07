import tkinter

from controlador.controlador import Controlador

class JanelaPrincipal(tkinter.Tk):
    def __init__(self, pinecone_api_key, huggingfacehub_api_key, *args, **kwargs):
        # Chamando o pai
        tkinter.Tk.__init__(self, *args, **kwargs)

        # Criando controlador
        self.controlador = Controlador(pinecone_api_key, huggingfacehub_api_key)

        # Definindo o título
        self.title("AS05: Implementação de Assistente Conversacional Baseado em LLM")

        # Configurando o tamanho da janela
        screen_width = 500
        screen_height = 350
        self.geometry(f"{screen_width}X{screen_height}+0+0")

        # Barra de menu
        barra_menu = tkinter.Menu(self)

        # Menu arquivo
        menu_arquivo = tkinter.Menu(barra_menu, tearoff=0)
        menu_arquivo.add_command(
            label="Abrir pasta com arquivos PDF",
            command=lambda: self.controlador.abrir_pasta_pdf()
        )
