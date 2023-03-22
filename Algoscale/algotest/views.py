from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .forms import TaskForm
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

class Crud(viewsets.ModelViewSet):

    def create_task(request):
        import pdb;pdb.set_trace()
        context={}
        form=TaskForm(request.POST)
        
        if request.method=="POST":
            if form.is_valid():
                form.save()
                #form.refresh_from_db()
                return redirect("/admin")
        else:
            form=TaskForm()
            context['form']=form
            return render(request,"create_task.html",context)
    
    def list_task(request):
        context={}
        #import pdb;pdb.set_trace()
        list_task=Task.objects.all()
        form=TaskForm(list_task)
        serializer=TaskSerializer(list_task,many=True)
        context['form']=serializer.data
        return render(request,'home.html',context)
    
    def list_id(request,id):
        context={}
    
        list_task=Task.objects.filter(pk=id)
        serializer=TaskSerializer(list_task,many=True)
        context['form']=serializer.data
        return render(request,'home.html',context)

    def update(request,id):
        id=Task.objects.get(pk=id)
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin')
        return render(request,'update.html',{'id':id})

    def delete(request,id):
        id=Task.objects.get(pk=id)
        id.delete()
        return HttpResponse("Task has been deleted")

