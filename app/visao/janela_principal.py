import tkinter

from visao.frame_chat import FrameChat


class JanelaPrincipal(tkinter.Tk):
    def __init__(self, controlador, *args, **kwargs):

        # Armazenando controlador
        self.controlador = controlador

        # Chamando o pai
        tkinter.Tk.__init__(self, *args, **kwargs)

        # Definindo o título
        self.title("AS05: Implementação de Assistente Conversacional Baseado em LLM")

        # Configurando o tamanho da janela
        screen_width = 500
        screen_height = 400
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        # Barra de menu
        barra_menu = tkinter.Menu(self)

        # Menu arquivo
        menu_arquivo = tkinter.Menu(barra_menu, tearoff=0)
        menu_arquivo.add_command(
            label="Abrir pasta com arquivos PDF",
            command=lambda: self.controlador.abrir_pasta_pdf()
        )

        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

        self.config(menu=barra_menu)

        # Frame do Chat
        self.frame_chat = FrameChat(self, self.controlador)
        self.frame_chat.pack(padx=10, pady=10, fill="both", expand=True)