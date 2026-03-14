from django.db import models
from django.utils import timezone

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

    def get_total_time(self):
        total_seconds = 0
        registros = self.timeregister_set.all()

        for registro in registros:
            if registro.finish:
                tempo = registro.finish - registro.start
            else:
                from django.utils import timezone
                tempo = timezone.now() - registro.start
            total_seconds += int(tempo.total_seconds())
        horas = total_seconds // 3600
        minutos = (total_seconds % 3600) // 60
        return f"{horas}h {minutos}m"

    def __str__(self):
        return f"{self.name} (Projeto: {self.project.name})"

class TimeRegister(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start = models.DateTimeField()
    finish = models.DateTimeField(null=True, blank=True)
    observation = models.TextField(blank=True, null=True)

    def get_duration(self):
        if self.finish:
            tempo_gasto = self.finish - self.start
        else:
            tempo_gasto = timezone.now() - self.start
        segundos_totais = int(tempo_gasto.total_seconds())
        horas = segundos_totais // 3600
        minutos = (segundos_totais % 3600) // 60
        return f"{horas}h {minutos}m"
    
    def __str__(self):
        return f"Registro de {self.task.name}"

    def __str__(self):
        return f"{self.task.name} - Início: {self.start} e Fim: {self.finish}"