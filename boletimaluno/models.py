from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    data_nascimento = models.DateField(max_length=255)

    def __str__(self) -> str:
        return f'{self.nome}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    carga_horaria = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.nome} :: {self.carga_horaria}'

    
class Boletim(models.Model):
    data_entrega = models.DateField(max_length=255)
    
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f'{self.aluno} :: {self.data_entrega}'

    
class BoletimNota(models.Model):
    nota = models.DecimalField(decimal_places=2, max_digits=10)
    
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    boletim = models.ForeignKey(Boletim, on_delete=models.CASCADE)
    