import email
from itertools import product
from django.shortcuts import redirect, render

from AppCRUD.models import EmployeeDetails

# Create your views here.

def addEmployee(request):
    return render(request,'addEmployee.html')

def index(request):
    return render(request,'index.html')

def add_employee_details(request):
    if request.method=='POST':
        eid=request.POST['employee_id']
        ename=request.POST['employee_name']
        edepartment=request.POST['employee_department']
        age=request.POST['employee_age']
        email=request.POST['employee_email']
        contact=request.POST['employee_contact']

        employee=EmployeeDetails(employee_id=eid,
                                employee_name=ename,
                                employee_department=edepartment,
                                employee_age=age,
                                employee_email=email,
                                employee_contact=contact)
        employee.save()
        print("hi..")
        return redirect('show_employees')

def show_employees(request):
    employees=EmployeeDetails.objects.all()
    return render(request,'showPimg.html',{'employee':employees})


def editpage(request,pk):
    employees=EmployeeDetails.objects.get(id=pk)
    
    return render(request,'edit.html',{'employee':employees})

def edit_employee_details(request,pk):
    if request.method=='POST':
        employee=EmployeeDetails.objects.get(id=pk)
        employee.employee_id=request.POST.get('employee_id')
        employee.employee_name=request.POST.get('employee_name')
        employee.employee_department=request.POST.get('employee_department')
        employee.employee_age=request.POST.get('employee_age')
        employee.employee_email=request.POST.get('employee_email')
        employee.employee_contact=request.POST.get('employee_contact')
        employee.save()
        return redirect('show_employees')
    return render(request,'edit.html')


def deletepage(request,pk):
    employees=EmployeeDetails.objects.get(id=pk)
    return render(request,'delete.html',{'employee':employees})

def delete_employee(request,pk):
    employees=EmployeeDetails.objects.get(id=pk)
    employees.delete()
    return redirect('show_employees')




