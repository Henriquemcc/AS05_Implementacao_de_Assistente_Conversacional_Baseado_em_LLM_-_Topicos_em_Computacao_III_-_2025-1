import tkinter

class FrameEntradaTexto(tkinter.Frame):
    def __init__(self, parent, controlador):
        tkinter.Frame.__init__(self, parent)

        # Guardando controlador
        self.controlador = controlador

        # Entrada de texto
        entrada_texto = tkinter.Entry(self)
        entrada_texto.pack(side="left", padx=5, fill="x", expand=True)
        entrada_texto.bind("<Return>", self.controlador.enviar_mensagem)

        # Botão enviar
        botao_enviar = tkinter.Button(self, text="Enviar", command=self.controlador.enviar_mensagem)
        botao_enviar.pack(side="right", padx=5)
