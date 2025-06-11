class Competidorfase1:
    def __init__(self, nome, idade, linguagens, matricula, semestre, universidade):
        self.nome = nome
        self.idade = idade
        self.linguagens = linguagens
        self.matricula = matricula
        self.semestre = semestre
        self.universidade = universidade

class Competidorfase2(Competidorfase1):
    def __init__(self, nome, idade, linguagens, matricula, semestre, universidade, aproveitamento, time):
        super().__init__(nome, idade, linguagens, matricula, semestre, universidade)
        self.aproveitamento = aproveitamento
        self.time = time

class Competidorfase3(Competidorfase2):
    def __init__(self, nome, idade, linguagens, matricula, semestre, universidade, aproveitamento, time, pais, documento, experiencia):
        super().__init__(nome, idade, linguagens, matricula, semestre, universidade, aproveitamento, time)
        self.pais = pais
        self.documento = documento
        self.experiencia = experiencia
        