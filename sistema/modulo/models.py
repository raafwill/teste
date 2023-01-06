from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Mentor(models.Model):
    nome = models.CharField(max_length=100)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    idade = models.IntegerField(default=0)