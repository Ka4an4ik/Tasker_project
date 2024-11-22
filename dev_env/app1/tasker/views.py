from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Task


def index(request):
    task_list = Task.objects.all().order_by('deadline_time')
    current_time = timezone.now()
    return render(request, "tasker/index.html", {"task_list": task_list, "current_time": current_time})


def task_view(request, task_id):
    task = get_object_or_404(Task, task_id=task_id) 
    return render(request, "tasker/event.html", {"task": task})  