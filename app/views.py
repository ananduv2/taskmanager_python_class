from django.shortcuts import render ,redirect
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
