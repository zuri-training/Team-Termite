
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login, logout


from .forms import UserCreation


# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def indexuser(request):
    return render(request, 'indexuser.html' )

@csrf_exempt
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('users:indexuser')
    else:
        if request.method == 'POST':
            username= request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('users:indexuser')
            else:
                    messages.info(request, 'Username or Password is incorrect')

        context ={}
        return render(request, 'login.html', context)

    
# def register(request):
#     return render(request, 'registration.html')

@csrf_exempt
def register(request): 
    if request.user.is_authenticated:
        return redirect('users:indexuser')
    else:
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


def logout_page(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')

def testimony(request):
    return render (request, 'testimonypage.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    return render(request, 'contact.html')

def category(request):
    return render(request, 'category.html')
