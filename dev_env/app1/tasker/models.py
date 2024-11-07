from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError



class User(models.Model):

    user_id = models.SmallIntegerField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=50)

    tasks = models.ManyToManyField("Task", through="User_Task")

    def __str__(self):
        return self.user_name


class Task(models.Model):

    task_id = models.SmallIntegerField(primary_key=True, unique=True)
    task_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    creation_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    deadline_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    priority = models.PositiveSmallIntegerField()
    readiness = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

    def checkout(self):
        if self.deadline_time and self.deadline_time < timezone.now():
            raise ValidationError("Дедлайн не может быть в прошлом.")




class User_Task(models.Model):

    foreign_user_id = models.ForeignKey("User", on_delete=models.PROTECT)
    foreign_task_id = models.ForeignKey("Task", on_delete=models.PROTECT)


    def __str__(self):
        return f"{self.foreign_user_id} - {self.foreign_task_id}"
