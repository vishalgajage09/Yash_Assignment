import re
from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'trainee/home.html')

def TraineeClick(request):
    return render(request,'trainee/traineeclick.html')

def Traineesignup(request):
    return render(request,'trainee/traineesignup.html')

def Traineelogin(request):
    return render(request,'trainee/traineelogin.html')