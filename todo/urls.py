from django.urls import path, include
from .views import signupuser

urlpatterns = [
    path('signupuser', signupuser, name='signupuser'),
    # path('signupuser', views.signupuser, name='signupuser'),

]
