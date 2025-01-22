from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_datetime
from .models import Task


def index(request):
    task_list = Task.objects.all().order_by("deadline_time")
    current_time = timezone.now()
    return render(
        request,
        "tasker/index.html",
        {"task_list": task_list, "current_time": current_time},
    )


def task_view(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    return render(request, "tasker/event.html", {"task": task})


def task_create(request):
    if request.method == "POST":
        task_name = request.POST.get("task_name")
        description = request.POST.get("description")
        deadline_time = request.POST.get("deadline_time")
        priority = request.POST.get("priority")

        deadline_time = parse_datetime(deadline_time)

        Task.objects.create(
            task_name=task_name,
            description=description,
            deadline_time=deadline_time,
            priority=priority,
        )

        return redirect("tasker:index")

    return render(request, "tasker/creatingTask.html")


def registration_view(request):
    return render(request, "registration/login.html")
