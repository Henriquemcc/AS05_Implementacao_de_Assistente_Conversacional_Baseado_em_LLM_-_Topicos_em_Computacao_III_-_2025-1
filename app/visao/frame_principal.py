import tkinter
from tkinter import scrolledtext
from visao.frame_entrada_texto import FrameEntradaTexto

class FramePrincipal(tkinter.Frame):
    def __init__(self, parent, controlador):
        # Chamando o pai
        tkinter.Frame.__init__(self, parent)

        # Guardando o controlador
        self.controlador = controlador

        # Área de saída do chat
        chat_text = scrolledtext.ScrolledText(self, wrap=tkinter.WORD, state='normal', height=20)
        chat_text.pack(padx=5, pady=5, fill="both", expand=True)

        # Entrada de texto
        frame_entrada_texto = FrameEntradaTexto(self, controlador)
        frame_entrada_texto.pack(fill="x", pady=5)


