from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'todo\home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo\signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:

                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'],)
                user.save()
                login(request, user)
                return redirect('current_todos')
            except IntegrityError:
                return render(request, 'todo\signup.html', {'form': UserCreationForm, 'error': IntegrityError})
        else:
            return render(request, 'todo\signup.html', {'form': UserCreationForm, 'error': IntegrityError})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo\loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'],)
        if user is None:
            return render(request, 'todo\loginuser.html', {'form': AuthenticationForm(), 'error': 'User not found, please validate User name and password'})
        else:
            login(request, user)
            return redirect('current_todos')


@login_required
def create_todo(request):
    if request.method == 'GET':
        return render(request, 'todo\create_todo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('current_todos')
        except ValueError:
            return render(request, 'todo\create_todo.html', {'form': TodoForm(), 'error': 'Bad request, please enter a proper data.'})


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def current_todos(request):
    todolist = Todo.objects.filter(
        user=request.user, datecompleted__isnull=True)
    return render(request, 'todo\currenttodos.html', {'todos': todolist})


@login_required
def view_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, r'todo\view_todo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('current_todos')
        except ValueError:
            return render(request, r'todo\view_todo.html', {'todo': todo, 'form': form, 'error': 'Bad request.'})


@login_required
def todo_completed(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('current_todos')


@login_required
def todo_delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('current_todos')


@login_required
def completed_todos(request):
    todolist = Todo.objects.filter(
        user=request.user, datecompleted__isnull=False)
    return render(request, 'todo\completedtodos.html', {'todos': todolist})
