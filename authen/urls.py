from django.urls import path
from .import views

urlpatterns = [
    path('', views.loginn, name='login'),
    path('signup', views.signupp, name='signup')
]