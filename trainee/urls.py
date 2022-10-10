from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('tclick/',views.TraineeClick),
    path('traineesignup/',views.Traineesignup,),
    path('traineelogin/',views.Traineelogin),


    # path('traineeclick/',views.TraineeClick,name='traineeclick')
    # path('traineeclick/',views.TraineeClick,name='traineeclick')
    # path('traineeclick/',views.TraineeClick,name='traineeclick')
    # path('traineeclick/',views.TraineeClick,name='traineeclick')
    # path('traineeclick/',views.TraineeClick,name='traineeclick')

]