from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signupuser(request):
    return render(request, 'todo\signup.html', {'form': UserCreationForm})