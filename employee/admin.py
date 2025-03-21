from django.contrib import admin
from .models import Unit
from .models import Employee

# Register your models here.
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
   list_display = ['id','name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
   list_display = ['id','name','age','phone','unit']