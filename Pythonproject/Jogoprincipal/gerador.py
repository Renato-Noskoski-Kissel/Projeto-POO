import random
from classes_fases import Competidorfase1, Competidorfase2, Competidorfase3

nomes = [
    "João","Lucas","Felipe","André","Maria","Beatriz","Ana","Juliana","Zorglon","Cynthi" #Corretos
    "Jo@o","Beatr!z","Maria123"] #Caracteres errados

linguagens = [
    "Python", "C++", "Java", "JavaScript", "Go", "Rust",  #Corretas
    "C#Script", "Git", " "]  #Inventadas

universidades = [
    "UFSC","USP","UFRJ","UNICAMP","UFMG","UFPE","UFRGS","UFPR",  # Corretas
    "UEEST","Harvard Brasil","USPTCC"]  #Inventadas

times = [
    "Alpha Coders","Bit Masters","Code Hackers","Syntax Team","DataStorm","Logic Lords","BugSlayers","ByteForge","Compilers","Backtrackers", #Correto
    "Techies","Coders","Team!!!"]  #Incorretos

semestres = [
        18.1, 18.2, 19.1, 19.2, 20.1, 20.2, 21.1, 21.2, 22.1, 22.2, 23.1, 23.2, 24.1, 24.2, 25.1, 25.2, #Corretos
        26.1, 26.2, 20.3, 30.1, 25.11 ] #Errados

paises = [
    "Brasil","Argentina","Canadá","Estados Unidos","França","Alemanha","Japão","Austrália", #Corretos
    "Narnia","Galrasia","Saara Ocidental"] #Inventados

def gerador_fase1():
    nome = random.choice(nomes)
    idade = random.randint(15, 31)
    linguagem = random.choice(linguagens)
    matricula = random.randint(18000000, 30999999)
    semestre = random.choice(semestres)
    universidade = random.choice(universidades)

    return Competidorfase1(nome, idade, linguagem, matricula, semestre, universidade)

def gerador_fase2():
    nome = random.choice(nomes)
    idade = random.randint(15, 31)
    linguagem = random.choice(linguagens)
    matricula = random.randint(18000000, 30999999)
    semestre = random.choice(semestres)
    universidade = random.choice(universidades)
    aproveitamento = round(random.uniform(60.0, 105.0), 1)
    time = random.choice(times)

    return Competidorfase2(nome, idade, linguagem, matricula, semestre, universidade, aproveitamento, time)

def gerador_fase3():
    nome = random.choice(nomes)
    idade = random.randint(15, 31)
    linguagem = random.choice(linguagens)
    matricula = random.randint(18000000, 30999999)
    semestre = random.choice(semestres)
    universidade = random.choice(universidades)
    aproveitamento = round(random.uniform(60.0, 105.0), 1)
    time = random.choice(times)
    pais = random.choice(paises)
    documento = random.randint(52345678900, 100000050888)
    experiencia = random.randint(0, 5)

    return Competidorfase3(nome, idade, linguagem, matricula, semestre, universidade, aproveitamento, time, pais, documento, experiencia)