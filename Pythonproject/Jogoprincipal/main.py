from tkinter import *
from PIL import Image, ImageTk
from gerador import gerador_fase1, gerador_fase2, gerador_fase3
from validacao import validar_fase1, validar_fase2, validar_fase3

root = Tk()
root.title("Papers, Please")

class Bemvindo:
    def __init__(self, master = None):
        self.master= master

        #definir fonte padrão e imagem que aparece no inicio
        self.fonte_padrao= ("Courier New", 14)
        self.img= Image.open("Jogoprincipal/Fotospy/fundo_oficial_fase1.png")
        self.imgtk = ImageTk.PhotoImage(self.img)

       #definindo as partes do menu:
        self.conteinerfundo = Label(master, image=self.imgtk)
        self.conteinerfundo.place(x=0, y=0, relwidth=1, relheight=1)
        self.master.bind("<Configure>", self.redimencionar)

        self.lista_regras = Button(font=self.fonte_padrao, text="Como selecionar?")
        self.lista_regras.place(x=1300, y=700)
        #self.lista_regras["command"] = self.Abrir_Lista_Regras

        self.conteiner_das_fases = Label(self.conteinerfundo, bg='#000c4d')
        self.conteiner_das_fases.place(relx = 0.5, rely=0.5, relwidth=0.7, relheight=0.7, anchor=CENTER)
        self.comecarjogo = Button(self.conteiner_das_fases, text="COMEÇAR JOGO", font="sel.font_padrao")
        self.comecarjogo.place(relx = 0.5, rely=0.5, relwidth=0.3, relheight=0.3, anchor=CENTER)
        self.comecarjogo["command"] = self.fase_atual()

    def fase_atual():
        

    def redimencionar(self, event):
        novo_height = event.height
        novo_width = event.width
        novotamanho = self.img.resize((novo_width, novo_height), Image.LANCZOS)
        self.imgtk = ImageTk.PhotoImage(novotamanho)
        self.conteinerfundo.config(image=self.imgtk)
        self.conteinerfundo.image = self.imgtk

app = Bemvindo(root)
root.mainloop()