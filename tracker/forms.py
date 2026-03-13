from django import forms
from .models import Project, Task, TimeRegister

#class Meta são ordens diretas que vou dar para o motor do Django

class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['name', 'description', 'active'] #colunas

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['project', 'name']

class TimeRegisterForm(forms.ModelForm):
  class Meta:
    model = TimeRegister
    fields = ['task', 'start', 'finish', 'observation']
    widgets = {
      'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
      'finish': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }