from tkinter import *
from PIL import Image, ImageTk
from gerador import gerador_fase1, gerador_fase2, gerador_fase3
from validacao import validar_fase1, validar_fase2, validar_fase3

root = Tk()
root.title("Papers, Please")
root.geometry("1000x700") # Define um tamanho inicial para a janela

class Bemvindo:
    def __init__(self, master=None):
        self.master = master
        self.fonte_padrao = ("Adobe Garamond Pro", 14)

        # Estado do Jogo
        self.fase_atual_numero = 1
        self.acertos_fase_atual = 0
        self.erros_fase_atual = 0
        self.competidor_atual = None
        self.erros_competidor_atual = [] # Para armazenar os erros do competidor atual

        # Dicionários para gerenciar as fases
        self.geradores = {1: gerador_fase1,
                          2: gerador_fase2,
                          3: gerador_fase3}
        self.validadores = {1: validar_fase1,
                            2: validar_fase2,
                            3: validar_fase3}
        self.max_acertos = {1: 5,
                            2: 5,
                            3: 5}
        self.max_erros = {1: 5,
                          2: 3,
                          3: 1}
        
        self.intro_images1 = Image.open("Jogoprincipal/Fotospy/fotoinicial.png")
        self.intro_images2 = Image.open("Jogoprincipal/Fotospy/foto1.png")
        self.intro_images3 = Image.open("Jogoprincipal/Fotospy/foto2.png")
        self.intro_images4 = Image.open("Jogoprincipal/Fotospy/foto3.png")
        self.intro_images1tk = ImageTk.PhotoImage(self.intro_images1)
        self.intro_images2tk = ImageTk.PhotoImage(self.intro_images2)
        self.intro_images3tk = ImageTk.PhotoImage(self.intro_images3)
        self.intro_images4tk = ImageTk.PhotoImage(self.intro_images4)
        self.containerfundo = Label(master, image=self.intro_images1tk)
        self.containerfundo.place(x=0, y=0, relwidth=1, relheight=1)
        self.imgatual = "Jogoprincipal/Fotospy/fotoinicial.png"
        self.master.bind("<Configure>", self.redimensionar)
        self.intro_counter = 0

        self.btn_prosseguir = Button(self.containerfundo, text="Prosseguir", font=("Adobe Garamond Pro", 18), bd=3, relief="raised",
                           bg="#e0e0e0", fg="#222", activebackground="#d5d5d5",
                           activeforeground="#000", highlightbackground="#b0b0b0", command=self.proximo_slide_intro)
        self.btn_prosseguir.place(relx=0.47, rely=0.9)
        
        # --- Widgets do Jogo (serão mostrados após "COMEÇAR JOGO") ---
        self.img_fundo = Image.open("Jogoprincipal/Fotospy/fundo_fases.png")
        self.img_fundotk = ImageTk.PhotoImage(self.img_fundo)
        self.game_frame = Frame(master)
        self.game_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.fundo_game_label = Label(self.game_frame, image=self.img_fundotk)
        self.fundo_game_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.game_frame.place_forget() # Esconde inicialmente
        self.info_competidor_label = Label(self.game_frame, text="", font=("Adobe Garamond Pro", 24), fg="white", bg="#6B6161", width=23, height=13,bd=5, relief=RIDGE, justify=CENTER)
        self.info_competidor_label.place(relx=0.03, rely=0.1)

        self.fase_status = Label(self.game_frame, text="Fase 1", font=("Franklin Gothic Heavy", 40), bg="#000000", fg="#c66a0f")
        self.fase_status.place(relx=0.434, rely=0.05)
        self.status_label = Label(self.game_frame, text="Acertos: 0 | Erros: 0", font=("Franklin Gothic Heavy", 30), fg="#ecc753", bg="#ffffff")
        self.status_label.place(relx=0.343, rely=0.9)
        self.competidor = Label(self.game_frame, text="Competidor", font=("Franklin Gothic Heavy", 30), fg="#ecc753", bg="#000000")
        self.competidor.place(relx=0.1, rely=0.025)


        self.btn_aceitar = Button(self.game_frame, text="ACEITAR", font=self.fonte_padrao, bg="green", fg="white", width=13, height=5, command=lambda: self.processar_decisao(True))
        self.btn_aceitar.place(relx=0.8, rely=0.33)

        self.btn_recusar = Button(self.game_frame, text="RECUSAR", font=self.fonte_padrao, bg="red", fg="white", width=13, height=5, command=lambda: self.processar_decisao(False))
        self.btn_recusar.place(relx=0.8, rely=0.57)

    def proximo_slide_intro(self):
        self.intro_counter += 1
        if self.intro_counter == 1:
            self.containerfundo.config(image=self.intro_images2tk)
            self.imgatual = "Jogoprincipal/Fotospy/foto1.png"
        elif self.intro_counter == 2:
            self.containerfundo.config(image=self.intro_images3tk)
            self.imgatual = "Jogoprincipal/Fotospy/foto2.png"
        elif self.intro_counter == 3:
            self.containerfundo.config(image=self.intro_images4tk)
            self.imgatual = "Jogoprincipal/Fotospy/foto3.png"
        else:
            self.btn_prosseguir.destroy()
            self.menu_inicial()

    def menu_inicial(self):
        # --- Configuração da Interface Inicial (Menu) ---
        self.img = Image.open("Jogoprincipal/Fotospy/fundo_oficial_fase1.png")
        self.imgmenutk = ImageTk.PhotoImage(self.img)

        self.containerfundo.config(image=self.imgmenutk)
        self.imgatual = "Jogoprincipal/Fotospy/fundo_oficial_fase1.png"

        self.lista_regras = Button(text="Como selecionar?",font=("Adobe Garamond Pro", 18), bd=3, relief="raised",
                           bg="#e0e0e0", fg="#222", activebackground="#d5d5d5",
                           activeforeground="#000", highlightbackground="#b0b0b0", command=self.Abrir_Lista_Regras)
        self.lista_regras.place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.1, anchor=CENTER)

        self.comecarjogo_btn = Button(text="COMEÇAR JOGO", font=("Adobe Garamond Pro", 18), bd=3, relief="raised",
                           bg="#e0e0e0", fg="#222", activebackground="#d5d5d5",
                           activeforeground="#000", highlightbackground="#b0b0b0", command=self.iniciar_nova_partida)
        self.comecarjogo_btn.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.2, anchor=CENTER)

        # --- Frame de Regras (Lateral):
        self.regras_frame = Frame(self.master, bg='#333333', bd=2, relief="groove")
        self.conteudo_regras = Text(self.regras_frame, wrap='word', font=(self.fonte_padrao[0], 8), fg='white', bg='#000c4d', width=40, height=30)
        self.conteudo_regras.insert('1.0', 'Livro de Regras\n', 'titulo')
        self.conteudo_regras.insert(END, 'Objetivo: Selecionar apenas candidatos com informações básicas válidas.\n\n', 'infos')
        self.conteudo_regras.insert(END, 'Fase 1: Inscrições\n\n', 'fase')
        self.conteudo_regras.insert(END, '- O nome é real (não é composto apenas por números ou símbolos).\n', 'normal')
        self.conteudo_regras.insert(END, '- A matrícula tem 8 dígitos e os dois primeiros indicam um ano até 2025.\n', 'normal')
        self.conteudo_regras.insert(END, '- O semestre é válido (ex: 22.1 ou 23.2).\n', 'normal')
        self.conteudo_regras.insert(END, '- A universidade está na lista oficial.\n', 'normal')
        self.conteudo_regras.insert(END, '- As linguagens são reais (ver lista de linguagens aceitas).\n\n', 'normal')
        self.conteudo_regras.insert(END, 'LISTAS\n\n', 'subtitulo')
        self.conteudo_regras.insert(END, 'Universidades válidas: UFSC - USP - UFRJ - UFMG - UNICAMP\n\n', 'normal')
        self.conteudo_regras.insert(END, 'Linguagens válidas: Python - C/C++ - Java - JavaScript - Go - Rust - TypeScript\n\n', 'normal')

        self.conteudo_regras.insert(END, 'Fase 2: Classificatórias\n\n', 'fase')
        self.conteudo_regras.insert(END, '- Todas as regras anteriores continuam válidas.\n', 'normal')
        self.conteudo_regras.insert(END, '- Aproveitamento é um número entre 70 e 100.\n', 'normal')
        self.conteudo_regras.insert(END, '- O nome do time tem pelo menos 2 palavras e parece real.\n\n', 'normal')

        self.conteudo_regras.insert(END, 'Fase 3: Finalistas Internacionais\n\n', 'fase')
        self.conteudo_regras.insert(END, '- Todas as regras anteriores continuam válidas.\n', 'normal')
        self.conteudo_regras.insert(END, '- O país é válido e reconhecido.\n', 'normal')
        self.conteudo_regras.insert(END, '- A experiência é um número entre 1 e 15 anos e corresponde com a idade do competidor.\n', 'normal')
        self.conteudo_regras.insert(END, '- O documento id tem 11 dígitos (como um CPF).\n\n', 'normal')
        self.conteudo_regras.insert(END, 'LISTAS\n\n', 'subtitulo')
        self.conteudo_regras.insert(END, 'Países aceitos: Brasil - Estados Unidos - Alemanha - Canadá - Japão - Argentina - França - Índia\n\n', 'normal')
        self.conteudo_regras.insert(END, 'Países banidos: Ilhas Fictícias - Qualquer país não reconhecido pela ONU - Países com nomes escritos incorretamente', 'normal')

        self.conteudo_regras.tag_config('fase', foreground='#07c4ff', font=('Arial', 25, 'bold'), justify=CENTER)
        self.conteudo_regras.tag_config('infos', font=('Arial', 18), justify=CENTER)
        self.conteudo_regras.tag_config('normal', font=('Arial', 12, 'bold'), justify=CENTER)
        self.conteudo_regras.tag_config('titulo', foreground='#07c4ff', font=('Arial', 30, 'bold'), justify=CENTER)
        self.conteudo_regras.tag_config('subtitulo', foreground="#a5daf5", font=('Arial', 15), justify=CENTER)
        self.conteudo_regras.pack(padx=10, pady=10, fill=BOTH, expand=True)

        self.botao_fechar_regras = Button(self.regras_frame, text="Fechar", command=self.Fechar_Lista_Regras, font=("Adobe Garamond Pro", 18), bd=3, relief="raised",
                           bg="#e0e0e0", fg="#222", activebackground="#d5d5d5",
                           activeforeground="#000", highlightbackground="#b0b0b0")
        self.botao_fechar_regras.pack(pady=5)

    def iniciar_nova_partida(self):
        # Esconde o menu inicial e mostra o frame do jogo
        self.containerfundo.place_forget()
        self.lista_regras.place_forget()
        self.comecarjogo_btn.place_forget()

        self.imgatualfases = "Jogoprincipal/Fotospy/fundo_fases.png"
        self.game_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.master.bind("<Configure>", self.redimensionarfases)
        self.game_frame.tkraise() # Garante que o frame do jogo esteja no topo

        # Reseta o estado do jogo para uma nova partida
        self.fase_atual_numero = 1
        self.acertos_fase_atual = 0
        self.erros_fase_atual = 0
        self.atualizar_status()
        self.proximo_competidor()

    def proximo_competidor(self):
        gerador = self.geradores[self.fase_atual_numero]
        validador = self.validadores[self.fase_atual_numero]

        self.competidor_atual = gerador()
        self.erros_competidor_atual = validador(self.competidor_atual)

        # Formata a informação do competidor para exibir
        info_str= ''
        for key in vars(self.competidor_atual):
            value = vars(self.competidor_atual)[key]
            info_str += f"{key.capitalize()}: {value}\n"
        self.info_competidor_label.config(text=info_str)

    def processar_decisao(self, aceitou_jogador):
        competidor_tem_erros = len(self.erros_competidor_atual) > 0

        if aceitou_jogador:
            if not competidor_tem_erros:
                self.acertos_fase_atual += 1
                # print("Competidor aceito corretamente!") # Para depuração
            else:
                self.erros_fase_atual += 1
                # print(f"Erro! Competidor aceito, mas tinha erros: {self.erros_competidor_atual}") # Para depuração
        else: # Recusou o jogador
            if competidor_tem_erros:
                self.acertos_fase_atual += 1
                # print("Competidor recusado corretamente!") # Para depuração
            else:
                self.erros_fase_atual += 1
                # print("Erro! Competidor recusado, mas era válido.") # Para depuração

        self.atualizar_status()
        self.verificar_progresso_fase()

    def atualizar_status(self):
        self.fase_status.config(text=f"Fase: {self.fase_atual_numero}")
        self.status_label.config(text=f"Acertos: {self.acertos_fase_atual}/{self.max_acertos[self.fase_atual_numero]} | Erros: {self.erros_fase_atual}/{self.max_erros[self.fase_atual_numero]}")

    def verificar_progresso_fase(self):
        if self.acertos_fase_atual >= self.max_acertos[self.fase_atual_numero]:
            # Avança para a próxima fase
            self.fase_atual_numero += 1
            if self.fase_atual_numero > 3: # Se passou de todas as fases
                self.mostrar_tela_final("vitoria")
            else:
                self.acertos_fase_atual = 0
                self.erros_fase_atual = 0
                self.atualizar_status()
                self.proximo_competidor()
                self.info_competidor_label.config(text=f"*** AVANÇANDO PARA FASE {self.fase_atual_numero} ***\n\nPreparando próximo competidor...")
                self.master.after(2000, self.proximo_competidor) # Pequena pausa para mostrar a mensagem de fase

        elif self.erros_fase_atual >= self.max_erros[self.fase_atual_numero]:
            self.mostrar_tela_final("gameover")

        else:
            self.proximo_competidor() # Próximo competidor na mesma fase

    def mostrar_tela_final(self, foto):
        self.game_frame.place_forget() # Esconde o jogo

        self.img_final_string = f"Jogoprincipal/Fotospy/{foto}.png"
        self.img_final = Image.open(f"Jogoprincipal/Fotospy/{foto}.png")
        self.imgfinaltk = ImageTk.PhotoImage(self.img_final)
        self.tela_final_frame = Frame(self.master)
        self.tela_final_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.fundo_game_label = Label(self.tela_final_frame, image=self.imgfinaltk)
        self.fundo_game_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.master.bind("<Configure>", self.redimensionarfinal)

        self.reiniciar_btn = Button(self.tela_final_frame, text="Reiniciar Jogo", font=("Adobe Garamond Pro", 20), bd=5, relief="raised", width=15, height=2, bg="#36668D", fg="white", activebackground="#306998", activeforeground="white", highlightbackground="#2b5a87", command=self.reiniciar_jogo)
        self.reiniciar_btn.place(relx = 0.25, rely = 0.8)

        self.sair_btn = Button(self.tela_final_frame, text="Sair", font=("Adobe Garamond Pro", 20), bd=5, relief="raised", width=15, height=2, bg="#A72823", fg="white", activebackground="#C9302C", activeforeground="white", highlightbackground="#912d2b", command=self.master.destroy)
        self.sair_btn.place(relx= 0.587, rely=0.8)

    def reiniciar_jogo(self):
        self.tela_final_frame.destroy() # Remove a tela final
        self.iniciar_nova_partida() # Inicia uma nova partida

    def Abrir_Lista_Regras(self):
        self.regras_frame.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)
        self.regras_frame.tkraise()

    def Fechar_Lista_Regras(self):
        self.regras_frame.place_forget()

    def redimensionar(self, event):
        self.img_redimencionada = Image.open(self.imgatual)
        novo_height = event.height
        novo_width = event.width
        if novo_width > 0 and novo_height > 0:
            novotamanho = self.img_redimencionada.resize((novo_width, novo_height), Image.LANCZOS)
            self.imgtk = ImageTk.PhotoImage(novotamanho)
            self.containerfundo.config(image=self.imgtk)
            self.containerfundo.image = self.imgtk # Manter referência

    def redimensionarfases(self, event):
        self.img_redimencionadafases = Image.open(self.imgatualfases)
        novo_height = event.height
        novo_width = event.width
        if novo_width > 0 and novo_height > 0:
            novotamanho = self.img_redimencionadafases.resize((novo_width, novo_height), Image.LANCZOS)
            self.imgtk = ImageTk.PhotoImage(novotamanho)
            self.fundo_game_label.config(image=self.imgtk)
            self.fundo_game_label.image = self.imgtk # Manter referência

    def redimensionarfinal(self, event):
        self.img_redimencionadafinal = Image.open(self.img_final_string)
        novo_height = event.height
        novo_width = event.width
        if novo_width > 0 and novo_height > 0:
            novotamanho = self.img_redimencionadafinal.resize((novo_width, novo_height), Image.LANCZOS)
            self.imgtk = ImageTk.PhotoImage(novotamanho)
            self.fundo_game_label.config(image=self.imgtk)
            self.fundo_game_label.image = self.imgtk # Manter referência

# Instancia a classe Bemvindo e inicia o loop principal do Tkinter
app = Bemvindo(root)
root.mainloop()