from django.shortcuts import render
from django.http import HttpResponse
from stdapp.models import Student,Department
from django.db.models import Q
import datetime
# Create your views here.
def index(request):
    return render(request,"index.html")

def all_std(request):
    std=Student.objects.all()
    context={
        'stds':std
    }
    return render(request,"all_std.html",context)

def add_std(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        Roll_No=request.POST['Roll_No']
        dept_obj = Department.objects.get(name=dept)
        new_std=Student(first_name=first_name,last_name=last_name,dept=dept_obj,Roll_No=Roll_No)
        new_std.save()
        return HttpResponse('Student added successfully')
    elif request.method =='GET':
        dept_list = Department.objects.all()
        return render(request, "add_std.html", {"dept_list": dept_list})
    else:
        return HttpResponse("An Exception Occured! Student has not Added")

def remove_std(request,std1_id = 0):
    if std1_id:
        try:
            std_to_be_removed=Student.objects.get(id=std1_id)
            std_to_be_removed.delete()
            return HttpResponse("Student removed successfully")
        except:
            return HttpResponse("Please enter a valid Student id")
    
    std=Student.objects.all()
    context={
        'stds':std
    }
    return render(request,"remove_std.html",context)

def filter_std(request):
    if request.method == 'POST':
        name=request.POST['name']
        dept=request.POST['dept']
        Roll_No=request.POST['Roll_No']
        stds=Student.objects.all()

        if name:
            stds=stds.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            stds=stds.filter(dept__name__icontains=dept)
        if Roll_No:
            stds=stds.filter(Roll_No=Roll_No)
        context={
            'stds':stds
        }

        return render(request,"all_std.html",context)
    elif request.method=='GET':
        return render(request,"filter_std.html")
    else:
        return HttpResponse("An Exception Occurred!")
    