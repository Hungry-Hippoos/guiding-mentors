from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
class loginPage:
    
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home1')
        else :
            messages.info(request,'Username or password incorrect')
    
    def get(self, request):
        context={}
        return render(request,'myApp/login.html',context)