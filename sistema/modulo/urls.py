from django.urls import path
from modulo import views

app_name = 'modulo'

urlpatterns = [
    path('aluno/', views.Alunos.as_view(), name='aluno'),
]