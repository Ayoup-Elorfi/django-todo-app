"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo.views import (
    signupuser,
    loginuser,
    current_todos,
    logoutuser,
    home_view,
    create_todo,
    view_todo,
    todo_completed,
    todo_delete,
    completed_todos,

)


urlpatterns = [

    # Auth URL's
    path('admin/', admin.site.urls),
    path('signupuser/', signupuser, name='signupuser'),
    path('loginuser/', loginuser, name='loginuser'),
    path('logout/', logoutuser, name='logout'),

    # Todo
    path('', home_view, name='home'),
    path('create/', create_todo, name='create_todo'),
    path('current/', current_todos, name='current_todos'),
    path('completed/', completed_todos, name='completed_todos'),
    path('todo/<int:todo_pk>', view_todo, name='view_todo'),
    path('todo/<int:todo_pk>/completed', todo_completed, name='todo_completed'),
    path('todo/<int:todo_pk>/delete', todo_delete, name='todo_delete'),


]
