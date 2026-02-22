from django.http import HttpResponse
from django.shortcuts import render
from employee.models import Employee

def home(request):
    employee_ = Employee.objects.all()
    context = {
        'employee_':employee_,
    }
    return render(request, 'home.html', context)
