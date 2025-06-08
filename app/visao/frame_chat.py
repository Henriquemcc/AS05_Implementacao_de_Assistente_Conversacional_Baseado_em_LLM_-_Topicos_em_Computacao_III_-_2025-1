import tkinter
from tkinter.scrolledtext import ScrolledText

class FrameChat(tkinter.Frame):
    def __init__(self, parent, controlador):
        tkinter.Frame.__init__(self, parent)
        self.controlador = controlador

        # Histórico de mensagens do chat
        self.historico = ScrolledText(self, wrap=tkinter.WORD, state='normal', height=20)
        self.historico.pack(padx=5, pady=5, fill="both", expand=True)

        # Frame da caixa de entrada de texto
        self.entrada_frame = tkinter.Frame(self)
        self.entrada_frame.pack(fill="x", pady=5)

        # Caixa de entrada de texto
        self.entrada_texto = tkinter.Entry(self.entrada_frame)
        self.entrada_texto.pack(side="left", padx=5, fill="x", expand=True)
        self.entrada_texto.bind("<Return>", self.__acao_enviar_mensagem)

        # Botão enviar
        self.botao_enviar = tkinter.Button(self.entrada_frame, text="Enviar", command=self.__acao_enviar_mensagem)
        self.botao_enviar.pack(side="right", padx=5)

    def __adicionar_mensagens_no_historico(self, mensagens):
        for mensagem in mensagens:
            self.historico.insert(tkinter.END, str(mensagem)+'\n')
            self.historico.see(tkinter.END)

    def __acao_enviar_mensagem(self, event=None):
        mensagem = self.entrada_texto.get()
        self.entrada_texto.delete(0, tkinter.END)
        self.controlador.enviar_mensagem(mensagem, lambda mensagens: self.__adicionar_mensagens_no_historico(mensagens))

    def set_cursor(self, state):
        # Configurando cursor no frame
        self.config(cursor=state)
        self.update()

        # Configurando cursor na entrada de texto
        self.entrada_texto.config(cursor=state)
        self.entrada_texto.update()

        # Configurando cursor no histório de chat
        self.historico.config(cursor=state)
        self.historico.update()