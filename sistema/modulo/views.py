from django.shortcuts import render
from django.views.generic import ListView
from modulo.models import Aluno, Mentor


# Create your views here.
class Alunos(ListView):
    template_name = 'alunos.html'
    # model = Aluno

    def get_queryset(self):
        a = Aluno.objects.filter()
        return a

