from django.shortcuts import render,redirect
from . models import Employee
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import AddEmployeeForm
# Create your views here.


def view_employee(request,id):
   if request.method == "GET":
      try:
         obj=Employee.objects.get(id=id)
      except Exception:
         return JsonResponse(data={"error":"Error"})
      pass

def delete_employee(request,id):
   if request.method == "POST":
      pass

def update_employee(request,id):
   if request.method == "PATCH":
      pass

def create_employee(request):
   if request.method == "POST":
      fm = AddEmployeeForm(request.POST)
      if fm.is_valid():
         fm.save()
         return redirect('home')
      else:
         return render(request,"create.html",{'form':fm})
   else:
      fm = AddEmployeeForm()
      return render(request,"create.html",{'form':fm})

def viewall_employee(request):
   if request.method == "GET":
      context = {"message" :"Hello this is the employee list "}
      return render(request, "view.html",context)
   
def home_employee(request):
   if request.method == "GET":
      context = {"message":"CRUD TABLE"}
      emp_data = Employee.objects.all()
      return render(request, "home.html",{'empdata':emp_data})