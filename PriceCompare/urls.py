from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('indexuser/', views.indexuser, name='indexuser'),
    path('logout/', views.logout_page, name='logout'),
    path('testimony/', views.testimony ,name='testimony'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact', views.contact, name='contact'),
    path('category', views.category,name='category'),
    path('dashboardcompare', views.dashboardcompare, name='dashboardcompare'),
    
]