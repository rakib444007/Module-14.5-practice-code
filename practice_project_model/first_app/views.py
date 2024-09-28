
# Create your views here.
from django.shortcuts import render,redirect

from first_app import models


def home(request):
    data =models.Student.objects.all()
    return render(request,'home.html',{'data' : data})