from django.urls import path
from . import views

app_name = 'tasker' 

urlpatterns = [
    path("", views.index, name="index"),  
    path("<int:task_id>/", views.task_view, name="view_task"), 
    path('register/', views.register, name='register'),
    path("creatingTask/",views.task_create,name="creating_task") 
]
