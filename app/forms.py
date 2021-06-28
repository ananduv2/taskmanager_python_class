from django.forms import ModelForm
from .models import *

class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields ='__all__'
