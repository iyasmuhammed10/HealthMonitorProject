from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from Hospitals import views as hos_Views
from django.contrib.auth.decorators import login_required
#view

def signin(request):
    if request.method == 'POST':
      
      username = request.POST["doc_id"]
      pass1 = request.POST['password']
      print("hi")
      if authenticate(request, username = username, password = pass1):
        is_user = User.objects.get(username=username)
        print(is_user)
        login(request, is_user)
        return redirect(home) 
      else:
        print('message')
        messages.error(request,"Bad Credentials")
        return redirect(signin)
    print('false')
    return render(request,"doctor_login.html")



@login_required(login_url="/doctors/login")
def home(request):
   if len(request.user.username) == 10:
        return redirect(hos_Views.home)
   return render(request, "home.html")