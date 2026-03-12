from django.urls import path
from . import views

urlpatterns = [
  path('', views.project_list, name='project_list'),
  path('novo-projeto/', views.project_create, name='project_create'),
  #Aqui novamente estou replicando o padrão de caminhos que usei nos projetos
  path('tarefas/', views.task_list, name='task_list'),
  path('nova-tarefa/', views.task_create, name='task_create')
]