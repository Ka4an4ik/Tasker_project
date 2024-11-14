from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.all().order_by('deadline_time')
    current_time = timezone.now()
    return render(request, "tasker/index.html", {"task_list": task_list, "current_time": current_time})