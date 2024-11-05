from django.contrib import admin

from main.models import Task, Project,Command

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Command)
