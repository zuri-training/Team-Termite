
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import UserCreation


# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginpage(request):

    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:index')
        else:
                messages.info(request, 'Username or Password is incorrect')

    context ={}
    return render(request, 'login.html', context)

    

def logoutuser(request):
    logout(request)

    return redirect('login')

# def register(request):
#     return render(request, 'registration.html')

def register(request): 
    form = UserCreation()  
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user )
            return redirect('login')
    context = {'form':form }  
    return render(request, 'registration.html', context) 