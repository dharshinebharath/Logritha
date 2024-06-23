from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.template.context_processors import csrf
from .models import Employees

def home(request):
    homepage=loader.get_template('home.html')
    return HttpResponse(homepage.render())

def all_emp(request):
    employees=Employees.objects.all()
    data={
        "employees":employees
    }
    return render(request,'employees.html',data)

def registration(request):
    #return HttpResponse("Registration Page")
    registrationpage=loader.get_template('form.html')
    return HttpResponse(registrationpage.render())

def add_emp(request):
    # form_data_page=loader.get_template('form_data.html')
    # return HttpResponse(form_data_page.render())
    if request.method=="GET":
        name=request.GET.get("name")
        department=request.GET.get("department")
        salary=request.GET.get("salary")
        bonus=request.GET.get("bonus")
        if (name is not None) and (department is not None) and (salary is not None) and (bonus is not None):
            Employees.objects.create(name=name,department=department,salary=salary,bonus=bonus)
            data={
                "name":name,"department":department,"salary":salary,"bonus":bonus,"message":"Employee Added Successfully"
            }
            return render(request,'form_data.html',data)

        else:
            data={
                "error_message":"Invalid Access",
            }
            return render(request,'form.html',data)


def remove_emp(request,id):
    
    print(id)
    emp=get_object_or_404(Employees,id=id)
    emp.delete()
    data={
        'message':"Employee Removed Successfully"
    }
    return render(request,'remove.html',data)


def update_form(request,id):
    
    emp=get_object_or_404(Employees,id=id)

    data={
        'emp':emp
    }
    return render(request,'update_form.html',data)

def update_form_data(request,id):
    
    emp=get_object_or_404(Employees,id=id)
    if request.method=="GET":
        name=request.GET.get("name")
        department=request.GET.get("department")
        salary=request.GET.get("salary")
        bonus=request.GET.get("bonus")
        if (name is not None) and (department is not None) and (salary is not None) and (bonus is not None):
            emp.name=name
            emp.department=department
            emp.salary=salary
            emp.bonus=bonus
            emp.save()
            data={
                "name":name,"department":department,"salary":salary,"bonus":bonus,"message":"Employee Updated Successfully"
            }
            return render(request,'update_form_data.html',data)

        else:
            data={
                "error_message":"Invalid Access",
            }
            return render(request,'update_form_data.html',data)
