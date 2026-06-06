from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_register(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_register')
    else:
        form = EmployeeForm()
    return render(request,'employee_register.html',{'form':form})
