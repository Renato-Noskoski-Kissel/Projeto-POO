import random
from classes_fases import Competidorfase1, Competidorfase2, Competidorfase3

nomes = [
    "Renato", "Mateus", "Stella", "Maicon", "Rodrigo", "Dornelles", "Manuela", "Luisa", "Vinicius", "Maria", "Victor", "Victorio", "Amanda", "Zafir", "Marco", "Julia", "Felipe", "Leticia", "Lara", "Renato", "Mateus", "Maicon",
    "Jo@o","Beatr!z","Maria123"] #Caracteres errados

linguagens = [
    "Python", "C++", "Java", "JavaScript", "Go", "Rust", "C", "Kotlin", "Perl", "Bash", "Typescript",  #Corretas
    "C#Script", "Git", " "]  #Inventadas

universidades = [
    "UFSC","USP","UFRJ","UNICAMP","UFMG","UFPE","UFRGS","UFPR", "UnB", "FURG", "UFBA", "UFAM", "IME-USP", "PUC-RS", "FURB", "PUC-PR", "Mackenzie", "ITA", "FAAP", "Feevale", "Unisul", # Corretas
    "UEEST","USPTCC", "HARVARD"]  #Inventadas

times = [
    "Alpha Coders","Bit Masters","Code Hackers","Syntax Team","Data Storm","Logic Lords","Bug Slayers","Byte Forge","Back Trackers", "Cyber Knights", "Byte Bandits", "Quantum Force", "Debug Masters", #Correto
    "Techies","Coders","Team!!!"]  #Incorretos

semestres = [21.1, 21.2, 22.1, 22.2, 23.1, 23.2, 24.1, 24.2, 25.1, 25.2]

paises = [
    "Brasil","Argentina","Canadá","Estados Unidos","França","Alemanha","Japão","Austrália", "India", "Reino Unido", "Russia", "China", #Corretos
    "Narnia","Galrasia","Saara Ocidental"] #Inventados

def gerador_fase1():
    nome = random.choice(nomes)
    idade = random.randint(17, 30)
    linguagem = random.choice(linguagens)
    semestre = random.choice(semestres)
    matricula = int((str(int(semestre*10))+str(random.randint(10000,99999))))
    universidade = random.choice(universidades)

    return Competidorfase1(nome, idade, linguagem, matricula, semestre, universidade)

def gerador_fase2():
    nome = random.choice(nomes)
    idade = random.randint(17, 30)
    linguagem = random.choice(linguagens)
    semestre = random.choice(semestres)
    matricula = int((str(int(semestre*10))+str(random.randint(10000,99999))))
    universidade = random.choice(universidades)
    aproveitamento = round(random.uniform(65.0, 102.0), 1)
    time = random.choice(times)

    return Competidorfase2(nome, idade, linguagem, matricula, semestre, universidade, aproveitamento, time)

def gerador_fase3():
    nome = random.choice(nomes)
    idade = random.randint(17, 30)
    linguagem = random.choice(linguagens)
    semestre = random.choice(semestres)
    matricula = int((str(int(semestre*10))+str(random.randint(10000,99999))))
    universidade = random.choice(universidades)
    aproveitamento = round(random.uniform(65.0, 101.0), 1)
    time = random.choice(times)
    pais = random.choice(paises)
    documento = random.randint(72345678900, 100000050888)
    experiencia = random.randint(0, 8)

    return Competidorfase3(nome, idade, linguagem, matricula, semestre, universidade, aproveitamento, time, pais, documento, experiencia)