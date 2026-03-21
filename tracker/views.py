from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Project, Task, TimeRegister
from .forms import ProjectForm, TaskForm, TimeRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
#view que lista os projetos
def project_list(request):
  projects = Project.objects.all()
  return render(request, 'tracker/project_list.html', {'projects': projects})

@login_required
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

@login_required
#Replicando o mesmo processo dos projetos para as Tarefas
def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'tracker/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('task_list')
  else:
    form = TaskForm()
  return render(request, 'tracker/task_form.html', {'form': form})

def time_list(request):
  times = TimeRegister.objects.all()
  return render(request, 'tracker/time_list.html', {'times': times})

def time_create(request):
  if request.method == 'POST':
    form = TimeRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('time_list')
  else: 
    form = TimeRegisterForm()
  return render(request, 'tracker/time_form.html', {'form': form})

@login_required
def start_timer(request, task_id):
  task = get_object_or_404(Task, id=task_id)
  TimeRegister.objects.create(
    task=task,
    start=timezone.now()
  )
  return redirect('task_list')

@login_required
def stop_timer(request, task_id):
  active_timer = TimeRegister.objects.filter(task_id=task_id, finish__isnull=True).first()
  if active_timer:
    active_timer.finish = timezone.now()
    active_timer.save()
  return redirect('task_list')