from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    concluded = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (Projeto: {self.project.name})"

class TimeRegister(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start = models.DateTimeField()
    finish = models.DateTimeField(null=True, blank=True)
    observation = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.task.name} - Início: {self.start} e Fim: {self.finish}"