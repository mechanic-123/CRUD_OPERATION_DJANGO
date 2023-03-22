from django.db import models

# Create your models here.

class Task(models.Model):
    status=(
        ('completed','completed'),
        ('pending','pending')
    )
    task_name=models.CharField(max_length=50,null=False,blank=False)
    description=models.CharField(max_length=150)
    duedate=models.DateField(auto_now=False, auto_now_add=False,blank=False,null=False)
    status=models.CharField(choices=status,max_length=50)


    def __str__(self):
        return f'{self.task_name}'

