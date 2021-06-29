from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth import logout,login as auth_login,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')

def validate_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        return HttpResponse("User validation failed")

def createuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =User.objects.create(username=username,password=password)
        user.set_password(password)
        user.save()
        return redirect('/')
    form = Login()
    context={'form': form}
    return render(request,'app/user.html',context)





def TaskList(request):
    user = request.user
    if user.is_anonymous:
        form = Login()
        context ={'form': form}
        return render(request,'app/login.html',context)
    task=Task.objects.filter(user=user)
    context={'task': task,'user': user}
    return render(request,'app/list.html',context)


def TaskCreate(request):
    user=request.user
    forms = CreateTask(initial={'user':user})
    forms.fields['user'].disabled = True
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
    


