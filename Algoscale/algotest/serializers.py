from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    # task_name=serializers.CharField()
    # description=serializers.CharField()
    # duedate=serializers.DateField()
    # status=serializers.CharField()
    