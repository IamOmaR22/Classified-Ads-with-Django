from django.shortcuts import render , redirect
from django.contrib import auth
from .forms import UserForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')

    else:
        user_form = UserForm()

    context = {'user_form' : user_form}

    return render(request , 'registration/register.html' , context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # set your success message here (like - You are now logged in)
            return redirect('home')
        else:
            # set your error message here (like - Invalid credentials)
            return redirect('login')
    else:
        return render(request, 'registration/login.html')
