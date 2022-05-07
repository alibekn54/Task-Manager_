from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(requests):
    tasks = Task.objects.all()
    return render(requests, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(requests):
    return render(requests, 'main/about.html')


def create(requests):
    error = ''
    if requests.method == 'POST':
        form = TaskForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(requests, 'main/create.html', context)
