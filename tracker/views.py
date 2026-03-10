from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

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