from django.contrib.auth import get_user_model
from django.db import models




# Create your models here.
class Command(models.Model):
    title = models.CharField(max_length=100)
    members = models.ManyToManyField(get_user_model())
    def count_members(self):
        return self.members.all().count()


class Task(models.Model):
    STATUS_CHOICES = (
        (0, 'Нужно сделать'),
        (1, 'В работе'),
        (2, 'Сделано'),
        (3, 'Доработать'),
        (4, 'Другое'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    status = models.CharField(default = 'Нужно сделать', max_length=20, choices= STATUS_CHOICES)




