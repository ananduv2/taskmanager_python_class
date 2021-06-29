from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields ='__all__'

class Login(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

