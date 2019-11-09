from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserCreateForm
from django.views.generic import CreateView
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
# Create your views here.



class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'


def logIn(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'You are log in')
            return redirect('home')
        else:
            messages.error(request,'Such a user not exist')
            return redirect('account:login')

    return render(request,'account/login.html')



@login_required
def logOut(request):
    logout(request)
    return redirect('home')