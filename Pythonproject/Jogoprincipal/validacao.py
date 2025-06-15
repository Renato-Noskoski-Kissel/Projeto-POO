def validar_fase1(COMPETIDOR):
    erros = []
    if COMPETIDOR.idade < 18 or COMPETIDOR.idade > 29:
        erros.append("Idade fora da faixa permitida")
    if COMPETIDOR.linguagens in ["C#Script", "Git", " "]:
        erros.append("Linguagem de programação inexistente")
    if COMPETIDOR.matricula > 25999999:
        erros.append("Matrícula incorreta")
    if COMPETIDOR.semestre in [26.1, 26.2, 20.3, 30.1, 25.11]:
        erros.append("Semestre inexistente")
    if COMPETIDOR.universidade in ["UEEST","USPTCC"]:
        erros.append("Universidade desconhecida")
    for letra in COMPETIDOR.nome:
        if letra in "1234567890!@#?":
            erros.append("Nomes com caracteres não permitidos")
            break
    return erros


def validar_fase2(COMPETIDOR):
    erros = validar_fase1(COMPETIDOR)
    if COMPETIDOR.aproveitamento < 70.0 or COMPETIDOR.aproveitamento > 100.0:
        erros.append("Aproveitamento insuficiente")
    if COMPETIDOR.time in ["Techies","Coders","Team!!!"]:
        erros.append("Nome do time não respeita as regas")
    return erros

def validar_fase3(COMPETIDOR):
    erros = validar_fase2(COMPETIDOR)
    if COMPETIDOR.pais in  ["Narnia","Galrasia","Saara Ocidental"]:
        erros.append("País não permitido")
    if COMPETIDOR.documento > 999999999999:
        erros.append("Documento Inválido")
    if (COMPETIDOR.idade - COMPETIDOR.experiencia) < 18:
        erros.append("Experiência não condiz com a idade do competidor")
    return erros
