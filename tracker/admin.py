from django.contrib import admin
from .models import Project, Task, TimeRegister

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TimeRegister)
