from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login')
    
]