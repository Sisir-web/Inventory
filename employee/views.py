from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from .forms import AddEmployeeForm

@login_required
def view_employee(request, id):
    """View a specific employee. Only unit heads or employees in the same unit can see them."""
    try:
        employee = CustomUser.objects.get(id=id)
        
        # Only allow if the user is in the same unit or is a superuser
        if request.user.ishead or request.user.unit == employee.unit or request.user.is_superuser:
            return render(request, "view_employee.html", {'employee': employee})
        else:
            return HttpResponseForbidden("You do not have permission to view this employee.")
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "Employee not found"}, status=404)

@login_required
def delete_employee(request, id):
    """Only unit heads can delete employees in their own unit."""
    employee = get_object_or_404(CustomUser, id=id)

    # Only allow if the user is a unit head and in the same unit
    if not request.user.ishead or request.user.unit != employee.unit:
        return HttpResponseForbidden("You do not have permission to delete this employee.")

    employee.delete()
    return redirect('home_employee')

@login_required
def update_employee(request, id):
    """Only unit heads can update employees in their own unit."""
    employee = get_object_or_404(CustomUser, id=id)

    if not request.user.ishead or request.user.unit != employee.unit:
        return HttpResponseForbidden("You do not have permission to update this employee.")

    if request.method == "POST":
        form = AddEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home_employee')
    else:
        form = AddEmployeeForm(instance=employee)

    return render(request, "update_employee.html", {'form': form})

@login_required
def create_employee(request):
    """Only unit heads can create employees within their unit."""
    if not request.user.ishead:
        return HttpResponseForbidden("You do not have permission to create employees.")

    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.unit = request.user.unit  # Assign same unit as the logged-in head
            employee.save()
            return redirect('home_employee')
    else:
        form = AddEmployeeForm()

    return render(request, "create.html", {'form': form})

@login_required
def viewall_employee(request):
    """Show only employees from the same unit as the logged-in user."""
    employees = CustomUser.objects.filter(unit=request.user.unit)
    return render(request, "view.html", {'employees': employees})

@login_required
def home_employee(request):
    """Show employees based on unit restrictions."""
    if request.user.is_superuser:
        employees = CustomUser.objects.all()  # Superuser sees all
    else:
        employees = CustomUser.objects.filter(unit=request.user.unit)  # Normal users see only their unit

    return render(request, "home.html", {'empdata': employees})
