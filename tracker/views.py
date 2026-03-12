from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm

#view que lista os projetos
def project_list(request):
  projects = Project.objects.all()
  return render(request, 'tracker/project_list.html', {'projects': projects})

#view que CRIA os projetos
def project_create(request):
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('project_list')
  else:
    form = ProjectForm()
    return render(request, 'tracker/project_form.html', {'form': form})
  
#Replicando o mesmo processo dos projetos para as Tarefas
def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'tracker/task_list.html', {'tasks': tasks})

def task_create(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('task_list')
  else:
    form = TaskForm()
  return render(request, 'tracker/task_form.html', {'form': form})