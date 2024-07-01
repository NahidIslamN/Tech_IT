from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout

from Authentications.models import Subsripbers

# Create your views here.


class Loging_Page (View):
    def get(self,request):
        return render(request,"login_page.html")
    
    def post(self,request):
        data = request.POST
        username = data.get("userName")
        password = data.get("password")
        if User.objects.filter(username = username ).exists():
            user = User.objects.get(username = username)
            if check_password(password, user.password):
                login(request,user)
            else:
                messages.info(request,"Wrong Password!")
                return redirect('/login/')
        else:
            messages.info(request,"Invalid Username!")
            return redirect('/login/')
                

        return redirect('/')


class LogoutRout(View):
    def get(self, request):
        logout(request)
        return redirect('/')
    

class Subscirber(View):
    def get(self, request):

        return redirect("/")
    
    def post(self,request):
        data = request.POST
        if Subsripbers.objects.filter(Email = data.get('email')).exists():
            messages.info(request,"Already Subscribed!")
            return redirect('/')
        else:
            obj = Subsripbers.objects.create(
                Email = data.get('email'),                        

            )
            obj.save()
            messages.info(request,"Thanks for subscribe us!")
            return redirect('/')
