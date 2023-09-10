from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_app/todo_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'todo_app/add_task.html', {'form': form})

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_app/update_task.html', {'form': form})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo_list')

def task_description(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'todo_app/task_description.html', {'task': task})