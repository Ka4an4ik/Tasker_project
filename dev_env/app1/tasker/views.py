from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
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


def task_create(request):
    return render(request,"tasker/creatingTask.html")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('tasker/index')  
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})