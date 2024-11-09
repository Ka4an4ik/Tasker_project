from django.urls import path

from . import views

app_name = 'tasker'

urlpatterns = [
    path("", views.index, name="index")
]