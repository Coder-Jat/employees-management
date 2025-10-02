from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.contrib import messages

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.position = request.POST.get('position')
        employee.department = request.POST.get('department')
        employee.email = request.POST.get('email')
        employee.save()
        messages.success(request, 'Employee details updated successfully!')
        return redirect('employee_list')
    
    return redirect('employee_list')
