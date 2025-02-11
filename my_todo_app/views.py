from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(title=form.cleaned_data['task'])
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'my_todo_app/create_task.html', {'form': form})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')


@csrf_exempt
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'completed': task.completed})