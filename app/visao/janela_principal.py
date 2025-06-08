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
        screen_height = 500
        self.geometry(f"{screen_width}x{screen_height}+0+0")

        # Barra de menu
        self.barra_menu = tkinter.Menu(self)

        # Menu arquivo
        menu_arquivo = tkinter.Menu(self.barra_menu, tearoff=0)
        menu_arquivo.add_command(
            label="Abrir pasta com arquivos PDF",
            command=lambda: self.controlador.abrir_pasta_pdf()
        )

        self.barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

        self.config(menu=self.barra_menu)

        # Frame do Chat
        self.frame_chat = FrameChat(self, self.controlador)
        self.frame_chat.pack(padx=10, pady=10, fill="both", expand=True)

    def set_cursor(self, state):
        # Configurando o cursor na janela
        self.config(cursor=state)
        self.update()

        # Configurando o cursor no frame
        self.frame_chat.set_cursor(state)

        # Configurando o cursor na barra de menu
        self.barra_menu.config(cursor=state)
        self.barra_menu.update()