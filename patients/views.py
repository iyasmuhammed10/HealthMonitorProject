
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib import messages

#view
def signin(request):
    if request.method == 'POST':
      
      username = request.POST["username"]
      pass1 = request.POST['pass1']

      user = authenticate(username = username, password = pass1)

      if user is not None:
          return redirect(home) 
      else:
        messages.error(request,"Bad Credentials")
        return redirect(signin)
    return render(request,"signin.html")

