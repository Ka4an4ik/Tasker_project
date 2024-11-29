from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError


class User(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=50,
        unique=False,
        blank=False,
        null=False,
        verbose_name="Username"
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    tasks = models.ManyToManyField("Task", through="User_Task")

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="tasker_user_groups",  
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="tasker_user_permissions",  
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Task(models.Model):

    task_id = models.AutoField(primary_key=True)
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
