from django.shortcuts import render
from .models import *

# Create your views here.

def TaskList(request):
    task=Task.objects.all()
    context={'task': task}
    return render(request,'app/list.html',context)
