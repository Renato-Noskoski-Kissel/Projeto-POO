from gerador import gerador_fase1, gerador_fase2, gerador_fase3
from validacao import validar_fase1, validar_fase2, validar_fase3


# Começa Fase 1:
def fase_atual(gerador, validador, max_acertos, max_erros):
    acertou_na_fase1 = 0
    errou_na_fase1 = 0
    print("PARA INICIAR DIGITE 'prosseguir'")
    digitou = input()
    if digitou == 'prosseguir':
        while True:
            COMPETIDOR = gerador()
            print(vars(COMPETIDOR))
            erros = validador(COMPETIDOR)
        
            print("PARA RECUSA-LO DIGITE '0', PARA ACEITA-LO DIGITE '1'")
            recusa_aceita = input()
            if len(erros) != 0 and recusa_aceita == '0':
                acertou_na_fase1 += 1
                print("Bom trabalho, ele era um impostor")
            elif len(erros) == 0 and recusa_aceita == '1':
                acertou_na_fase1 += 1
                print("Bom trabalho")
            else:
                errou_na_fase1 += 1
                print(erros)
            if acertou_na_fase1 == max_acertos:
                return True
            elif errou_na_fase1 == max_erros:
                print("Os impostores tomaram conta, GAME OVER!")
                return False
         
#Isso aq faz com que se deu game over, volte para a fase 1
def main():
    while True:
        if fase_atual(gerador_fase1, validar_fase1, 5, 5) == False:
            continue
        elif fase_atual(gerador_fase2, validar_fase2, 5, 3) == False:
            continue
        elif fase_atual(gerador_fase3, validar_fase3, 5, 1) == False:
            continue
        else:
            break
    print("PARABENS VC GANHOU!!!!!")
main()
