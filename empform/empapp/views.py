from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.
def emp_view(request):
    emp=EmployeeForm()
    return render(request,'emp.html',{'emp1':emp})
