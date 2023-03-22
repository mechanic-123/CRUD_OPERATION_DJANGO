from django.contrib import admin
from .models import Task

# Register your models here.

#admin.site.register(Task)

@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display=('task_name','description','duedate','status')
   