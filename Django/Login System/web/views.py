from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import userModel
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

login_required(login_url='loginpage')
def home(request):
    return render(request, 'home.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

def registerpage(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    return render(request,'register.html',{'form':form})


login_required(login_url='loginpage')
def logoutpage(request):
    logout(request)
    return redirect('home')