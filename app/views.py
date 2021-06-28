from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def TaskList(request):
    user = request.user
    task=Task.objects.all()
    context={'task': task,'user': user}
    return render(request,'app/list.html',context)


def TaskCreate(request):
    forms = CreateTask()
    if request.method == 'POST':
        forms = CreateTask(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context={'forms': forms}
    return render(request,'app/create.html',context)


def TaskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    forms = CreateTask(instance=task)
    if request.method == 'POST':
        forms = CreateTask(request.POST,instance=task)
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context={'forms': forms}
    return render(request,'app/create.html',context)


def TaskDelete(request,pk):
    task = get_object_or_404(Task, id = pk)
    task.delete()
    return redirect('/')
    


