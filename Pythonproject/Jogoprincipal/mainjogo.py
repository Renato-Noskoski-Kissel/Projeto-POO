from gerador import gerador_fase1, gerador_fase2, gerador_fase3

verificarfase1 = False
fase2 = False
fase3 = False

# Começa Fase 1:
def fase1():
    acertou_na_fase1 = 0
    errou_na_fase1 = 0
    print("PARA INICIAR DIGITE 'prosseguir'")
    digitou = input()
    if digitou == 'prosseguir':
        while True:
            COMPETIDOR = gerador_fase1()
            print(vars(COMPETIDOR))
            atual_errado = False

            if COMPETIDOR.idade < 18 or COMPETIDOR.idade > 29:
                atual_errado = True
            elif COMPETIDOR.linguagens in ["C#Script", "Git", " "]:
                atual_errado = True
            elif COMPETIDOR.matricula > 25999999:
                atual_errado = True
            elif COMPETIDOR.semestre in [26.1, 26.2, 20.3, 30.1, 25.11]:
                atual_errado = True
            elif COMPETIDOR.universidade in ["UEEST","Harvard Brasil","USPTCC"]:
                atual_errado = True
            else:
                for letra in COMPETIDOR.nome:
                    if letra in "1234567890!@#?":
                        atual_errado = True
                        break
            #Verificar se o competidor é impostor ou não
            print("PARA RECUSA-LO DIGITE '0', PARA ACEITA-LO DIGITE '1'")
            recusa_aceita = input()
            if atual_errado == True and recusa_aceita == '0':
                acertou_na_fase1 += 1
                print("Bom trabalho, ele era um impostor")
            elif atual_errado == False and recusa_aceita == '1':
                acertou_na_fase1 += 1
                print("Bom trabalho")
            else:
                errou_na_fase1 += 1
                print("Cuidado, ele era um impostor!")
            if acertou_na_fase1 == 5:
                print("Você passou da fase 1!")
                return True
            elif errou_na_fase1 == 5:
                print("Os impostores tomaram conta, GAME OVER!")
                return False


# Começa Fase 2:
def fase2():
    acertou_na_fase2 = 0
    errou_na_fase2 = 0
    print("PARA INICIAR A FASE 2 DIGITE 'prosseguir'")
    digitou = input()
    if digitou == 'prosseguir':
        while True:
            COMPETIDOR = gerador_fase2()
            print(vars(COMPETIDOR))
            atual_errado = False

            if COMPETIDOR.idade < 18 or COMPETIDOR.idade > 29:
                atual_errado = True
            elif COMPETIDOR.linguagens in ["C#Script", "Git", " "]:
                atual_errado = True
            elif COMPETIDOR.matricula > 25999999:
                atual_errado = True
            elif COMPETIDOR.semestre in [26.1, 26.2, 20.3, 30.1, 25.11]:
                atual_errado = True
            elif COMPETIDOR.universidade in ["UEEST","Harvard Brasil","USPTCC"]:
                atual_errado = True
            elif COMPETIDOR.aproveitamento < 70.0 and COMPETIDOR.aproveitamento > 100.0:
                atual_errado = True
            elif COMPETIDOR.time in ["Techies","Coders","Team!!!"]:
                atual_errado = True
            else:
                for letra in COMPETIDOR.nome:
                    if letra in "1234567890!@#?":
                        atual_errado = True
                        break
        
            #Verificar se o competidor é impostor ou não
            print("PARA RECUSA-LO DIGITE '0', PARA ACEITA-LO DIGITE '1'")
            recusa_aceita = input()
            if atual_errado == True and recusa_aceita == '0':
                acertou_na_fase2 += 1
                print("Bom trabalho, ele era um impostor")
            elif atual_errado == False and recusa_aceita == '1':
                acertou_na_fase2 += 1
                print("Bom trabalho")
            else:
                errou_na_fase2 += 1
                print("Cuidado, ele era um impostor!")
            if acertou_na_fase2 == 5:
                print("Você passou da fase 2!")
                return True
            elif errou_na_fase2 == 3:
                print("Os impostores tomaram conta, GAME OVER!")
                return False

# Começa Fase 3:
def fase3():
    acertou_na_fase3 = 0
    errou_na_fase3 = 0
    print("PARA INICIAR A FASE 3 DIGITE 'prosseguir'")
    digitou = input()
    if digitou == 'prosseguir':
        while True:
            COMPETIDOR = gerador_fase3()
            print(vars(COMPETIDOR))
            atual_errado = False

            if COMPETIDOR.idade < 18 or COMPETIDOR.idade > 29:
                atual_errado = True
            elif COMPETIDOR.linguagens in ["C#Script", "Git", " "]:
                atual_errado = True
            elif COMPETIDOR.matricula > 25999999:
                atual_errado = True
            elif COMPETIDOR.semestre in [26.1, 26.2, 20.3, 30.1, 25.11]:
                atual_errado = True
            elif COMPETIDOR.universidade in ["UEEST","Harvard Brasil","USPTCC"]:
                atual_errado = True
            elif COMPETIDOR.aproveitamento < 70.0 and COMPETIDOR.aproveitamento > 100.0:
                atual_errado = True
            elif COMPETIDOR.time in ["Techies","Coders","Team!!!"]:
                atual_errado = True
            elif COMPETIDOR.pais in  ["Narnia","Galrasia","Saara Ocidental"]:
                atual_errado = True
            elif COMPETIDOR.documento > 999999999999:
                atual_errado = True
            elif COMPETIDOR.idade - COMPETIDOR.experiencia < 15:
                atual_errado = True
            else:
                for letra in COMPETIDOR.nome:
                    if letra in "1234567890!@#?":
                        atual_errado = True
                        break
        
            #Verificar se o competidor é impostor ou não
            print("PARA RECUSA-LO DIGITE '0', PARA ACEITA-LO DIGITE '1'")
            recusa_aceita = input()
            if atual_errado == True and recusa_aceita == '0':
                acertou_na_fase3 += 1
                print("Bom trabalho, ele era um impostor")
            elif atual_errado == False and recusa_aceita == '1':
                acertou_na_fase3 += 1
                print("Bom trabalho")
            else:
                errou_na_fase3 += 1
                print("Cuidado, ele era um impostor!")
            if acertou_na_fase3 == 5:
                print("Você passou da fase 3!")
                return True
            elif errou_na_fase3 == 1:
                print("Os impostores tomaram conta, GAME OVER!")
                return False
            
#Isso aq faz com que se deu game over, volte para a fase 1
def main():
    while True:
        if fase1() == False:
            continue
        elif fase2() == False:
            continue
        elif fase3() == False:
            continue
        else:
            break
    print("PARABENS VC GANHOU!!!!!")

main()
    
    
