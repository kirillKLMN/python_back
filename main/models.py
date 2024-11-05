from django.contrib.auth import get_user_model
from django.db import models




# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_end = models.DateField()
    date_start = models.DateField()
    leader = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

class Command(models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Task(models.Model):
    STATUS_CHOICES = (
        ('Нужно сделать', 'Нужно сделать'),
        ('В работе', 'В работе'),
        ('Сделано', 'Сделано'),
        ('Доработать', 'Доработать'),
        ('Другое', 'Другое'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=())
    assigned = models.BooleanField(default=False)




