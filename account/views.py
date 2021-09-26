from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import login,logout,authenticate
from django.db import connection

# Create your views here.


def user_login(request):
    return render(request,'login.html')


def user_reg(request):
    return render(request,'reg.html')



def user_reg_action(request):
    cursor=connection.cursor()
    if request.method=='POST':
        username=request.POST['uname']
        password1=request.POST['password1']
        password2=request.POST['password2']
        len_calc=len(username)

        if User.objects.filter(username=username).exists():
            msg="<script>alert('username is already taken'); window.location='/account/user_reg';</script>"
            return HttpResponse(msg)
        
        elif (len_calc==0):
            msg="<script>alert('Must enter Username'); window.location='/account/user_reg';</script>"
            return HttpResponse(msg)

        elif (len_calc<6):
            msg="<script>alert('username must contain atleast 6 characters'); window.location='/account/user_reg';</script>"
            return HttpResponse(msg)

        elif (password1!=password2):
            msg="<script>alert('confirm password'); window.location='/account/user_reg';</script>"
            return HttpResponse(msg)
        else:
            pass


        if password1==password2:
            user=User.objects.create_user(username=username,password=password1)
            user.save()
            return redirect('user_login')
        else:
            return redirect('user_reg')
    else:
        return redirect("user_reg")



def user_login_action(request):
    if request.method=='POST':
        username=request.POST['uname']
        password1=request.POST['password1']
        
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect("user_login")
        
    else:
        return redirect("user_reg")


def user_logout(request):
    logout(request)
    return redirect("/")