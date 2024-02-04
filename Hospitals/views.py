from django.shortcuts import render,redirect
from doctors.models import *
from patients.models import *
from doctors import views as doc_Views
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random

# Create your views here.
@login_required(login_url="/hospitals/login")
def home(request):
    if len(request.user.username) == 8:
        return redirect(doc_Views.home)
    doc_det = DoctorDetails.objects.all()
    Doc_id = random.randrange(11111111, 99999999)
    print(Doc_id)
    while DoctorDetails.objects.filter(Doc_id=Doc_id):
            if Doc_id != doc_det.Doc_id:
                break
            Doc_id = random.randrange(11111111, 99999999)
    return render(request, "hospital.html", {"Doc_id":Doc_id})

#view
def signin(request):
    if request.method == 'POST':
      
      username = request.POST["hospitalID"]
      pass1 = request.POST['password']
      print(username)
    
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
    return render(request,"hospital_login.html")

@login_required(login_url="/hospitals/login")
def addpatient(request):
    
    if request.user.is_authenticated:
        Hos_id = request.user.username
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        phone_number0 = request.POST['phone_number0']
        phone_number1 = request.POST['phone_number1']
        sex = request.POST['sex']
        device_ID = request.POST['device_ID']
        password = request.POST['password']
        Doc_id = request.POST['Doc_id']

        if Patients_Details.objects.filter(device_ID=device_ID):
            messages.error(request, "Device ID Already Registered!!")
            return redirect(home)
        user = User.objects.create(
            password =password,
            username =device_ID

        )
        user.save()

        Patients_Details.objects.create(
            name=name,
            age=age,
            phone_number0=phone_number0,
            phone_number1=phone_number1,
            sex=sex,
            device_ID=device_ID,
            password=password,
            Doc_id=Doc_id,
            Hos_id=Hos_id
        )
    return redirect(home)


def adddoctor(request):
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            Hos_id = request.user.username
            name = request.POST['name']
            Doc_id = request.POST['Doc_id']
        if DoctorDetails.objects.filter(Doc_id=Doc_id):
            messages.error(request, "Doctor with this Doc ID Already Registered!!")
            return redirect(home)
        user = User.objects.create(
                password=name,
                username=Doc_id

        )
        user.save()
        DoctorDetails.objects.create(
                name=name,
                Doc_id=Doc_id,
                Hos_id=Hos_id
            )
        
    return redirect(home)