from django.shortcuts import render
from .models import Employee

# Create your views here.

def employee(request):
    stud=Employee.objects.all()
    return render(request,'employee.html',{'emp':stud})
