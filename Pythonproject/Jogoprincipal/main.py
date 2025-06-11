from tkinter import *
from PIL import Image, ImageTk
# Importe as funções de gerador e validação
from gerador import gerador_fase1, gerador_fase2, gerador_fase3
from validacao import validar_fase1, validar_fase2, validar_fase3

# O Tkinter root deve ser criado uma única vez
root = Tk()
root.title("Papers, Please")
root.geometry("1000x700") # Define um tamanho inicial para a janela

class Bemvindo:
    def __init__(self, master=None):
        self.master = master
        self.fonte_padrao = ("Courier New", 14)

        # Estado do Jogo
        self.fase_atual_numero = 1
        self.acertos_fase_atual = 0
        self.erros_fase_atual = 0
        self.competidor_atual = None
        self.erros_competidor_atual = [] # Para armazenar os erros do competidor atual

        # Dicionários para gerenciar as fases
        self.geradores = {
            1: gerador_fase1,
            2: gerador_fase2,
            3: gerador_fase3
        }
        self.validadores = {
            1: validar_fase1,
            2: validar_fase2,
            3: validar_fase3
        }
        self.max_acertos = {
            1: 5,
            2: 5,
            3: 5
        }
        self.max_erros = {
            1: 5,
            2: 3,
            3: 1
        }

        # --- Configuração da Interface Inicial (Menu) ---
        self.img = Image.open("Jogoprincipal/Fotospy/fundo_oficial_fase1.png")
        self.imgtk = ImageTk.PhotoImage(self.img)

        self.containerfundo = Label(master, image=self.imgtk)
        self.containerfundo.place(x=0, y=0, relwidth=1, relheight=1)
        self.master.bind("<Configure>", self.redimensionar)

        self.lista_regras = Button(font=self.fonte_padrao, text="Como selecionar?", command=self.Abrir_Lista_Regras)
        self.lista_regras.place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.1, anchor=CENTER)

        self.container_das_fases = Label(self.containerfundo, bg='#000c4d')
        self.container_das_fases.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.7, anchor=CENTER)

        self.comecarjogo_btn = Button(self.container_das_fases, text="COMEÇAR JOGO", font=self.fonte_padrao, command=self.iniciar_nova_partida)
        self.comecarjogo_btn.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3, anchor=CENTER)

        # --- Frame de Regras (Lateral) ---
        self.regras_frame = Frame(master, bg='#333333', bd=2, relief="groove")
        self.conteudo_regras = Label(self.regras_frame, text=(
        "|Livro de Regras|Fase 1: Inscrição|Objetivo: Selecionar apenas candidatos com informações básicas válidas.|✅ Aceite se:|O nome é real (não é composto apenas por números ou símbolos).|A matrícula tem 8 dígitos e os dois primeiros indicam um ano existente até 2025 (ex: 25xxxxxx está ok, mas 26xxxxxx não).|O semestre é válido (ex: 22.1 ou 23.2 – valores como 23.9 ou 21.7 são inválidos).|A universidade está na lista oficial (exemplos abaixo).|As linguagens são reais (ver lista de linguagens aceitas).|📄 Universidades válidas:UFSC - USP - UFRJ - UFMG - UNICAMP|🧠 Linguagens válidas:Python - C/C++ - Java - JavaScript - Go - Rust - TypeScript|Fase 2: Classificatórias|Objetivo: Garantir que só avancem candidatos com bom desempenho e que estejam em times válidos.|✅ Aceite se:|Todas as regras da Fase 1 ainda valem.|Aproveitamento é um número entre 70 e 100 (mínimo exigido).|O nome do time tem pelo menos 2 palavras e parece real (ex: Time UFSC, Os Recursivos, Dev Fighters).|Fase 3: Finalistas Internacionais|Objetivo: Somente os melhores e com dados corretos podem representar o país.|✅ Aceite se:|Todas as regras da Fase 1 e Fase 2 continuam válidas.|O país é válido e reconhecido.|A experiência é um número entre 1 e 15 anos.|O documento id tem 11 dígitos (como um CPF).|🌎 Países aceitos: Brasil - Estados Unidos - Alemanha - Canadá - Japão - Argentina - França - Índia |🚫 Países banidos: Ilhas Fictícias - Qualquer país não reconhecido pela ONU - Países com nomes escritos incorretamente"
        ), font=(self.fonte_padrao[0], 8), fg="white", bg='#000c4d', wraplength=270, justify=LEFT)
        self.conteudo_regras.pack(padx=10, pady=10, fill=BOTH, expand=True)

        self.botao_fechar_regras = Button(self.regras_frame, text="X Fechar", command=self.Fechar_Lista_Regras, font=(self.fonte_padrao[0], 10))
        self.botao_fechar_regras.pack(pady=5)

        # --- Widgets do Jogo (serão mostrados após "COMEÇAR JOGO") ---
        self.game_frame = Frame(master, bg='#131044')
        self.game_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self.game_frame.place_forget() # Esconde inicialmente
        self.info_competidor_label = Label(self.game_frame, text="", font=self.fonte_padrao, fg="white", bg="#131044", wraplength=400, justify=LEFT)
        self.info_competidor_label.pack(pady=20, padx=20, anchor=NW)

        self.status_label = Label(self.game_frame, text="Fase: 1 | Acertos: 0 | Erros: 0", font=self.fonte_padrao, fg="yellow", bg="#131044")
        self.status_label.pack(pady=10, anchor=N)

        self.btn_aceitar = Button(self.game_frame, text="ACEITAR", font=self.fonte_padrao, bg="green", fg="white", command=lambda: self.processar_decisao(True))
        self.btn_aceitar.pack(side=LEFT, padx=50, pady=20, anchor=S)

        self.btn_recusar = Button(self.game_frame, text="RECUSAR", font=self.fonte_padrao, bg="red", fg="white", command=lambda: self.processar_decisao(False))
        self.btn_recusar.pack(side=RIGHT, padx=50, pady=20, anchor=S)

    def iniciar_nova_partida(self):
        # Esconde o menu inicial e mostra o frame do jogo
        self.containerfundo.place_forget()
        self.container_das_fases.place_forget()
        self.lista_regras.place_forget()
        self.comecarjogo_btn.place_forget()

        self.game_frame.place(x=0, y=0, relwidth=1, relheight=1)
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
        info_str = "Competidor:\n"
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
        self.status_label.config(text=f"Fase: {self.fase_atual_numero} | Acertos: {self.acertos_fase_atual}/{self.max_acertos[self.fase_atual_numero]} | Erros: {self.erros_fase_atual}/{self.max_erros[self.fase_atual_numero]}")

    def verificar_progresso_fase(self):
        if self.acertos_fase_atual >= self.max_acertos[self.fase_atual_numero]:
            # Avança para a próxima fase
            self.fase_atual_numero += 1
            if self.fase_atual_numero > 3: # Se passou de todas as fases
                self.mostrar_tela_final("Parabéns, você GANHOU O JOGO!")
            else:
                self.acertos_fase_atual = 0
                self.erros_fase_atual = 0
                self.atualizar_status()
                self.proximo_competidor()
                self.info_competidor_label.config(text=f"*** AVANÇANDO PARA FASE {self.fase_atual_numero} ***\n\nPreparando próximo competidor...")
                self.master.after(2000, self.proximo_competidor) # Pequena pausa para mostrar a mensagem de fase

        elif self.erros_fase_atual >= self.max_erros[self.fase_atual_numero]:
            self.mostrar_tela_final("Game Over! Os impostores tomaram conta.")

        else:
            self.proximo_competidor() # Próximo competidor na mesma fase

    def mostrar_tela_final(self, mensagem):
        self.game_frame.place_forget() # Esconde o jogo

        self.tela_final_frame = Frame(self.master, bg='#000c4d')
        self.tela_final_frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.6, anchor=CENTER)

        self.mensagem_final_label = Label(self.tela_final_frame, text=mensagem, font=("Courier New", 20, "bold"), fg="yellow", bg='#000c4d', wraplength=600, justify=CENTER)
        self.mensagem_final_label.pack(pady=50)

        self.reiniciar_btn = Button(self.tela_final_frame, text="Reiniciar Jogo", font=self.fonte_padrao, command=self.reiniciar_jogo)
        self.reiniciar_btn.pack(pady=20)

        self.sair_btn = Button(self.tela_final_frame, text="Sair", font=self.fonte_padrao, command=self.master.destroy)
        self.sair_btn.pack(pady=10)

    def reiniciar_jogo(self):
        self.tela_final_frame.destroy() # Remove a tela final
        self.iniciar_nova_partida() # Inicia uma nova partida

    def Abrir_Lista_Regras(self):
        self.regras_frame.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)
        self.regras_frame.tkraise()

    def Fechar_Lista_Regras(self):
        self.regras_frame.place_forget()

    def redimensionar(self, event):
        novo_height = event.height
        novo_width = event.width
        if novo_width > 0 and novo_height > 0:
            novotamanho = self.img.resize((novo_width, novo_height), Image.LANCZOS)
            self.imgtk = ImageTk.PhotoImage(novotamanho)
            self.containerfundo.config(image=self.imgtk)
            self.containerfundo.image = self.imgtk # Manter referência


# Instancia a classe Bemvindo e inicia o loop principal do Tkinter
app = Bemvindo(root)
root.mainloop()