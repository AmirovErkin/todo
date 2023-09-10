from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'description']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'})
        }