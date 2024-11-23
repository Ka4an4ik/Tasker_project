from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Task

class TaskExclude(admin.ModelAdmin):
    exclude = ('readiness',)


admin.site.site_header = "Tasker Editor" 
admin.site.index_title = "Override"

admin.site.register(Task, TaskExclude)

