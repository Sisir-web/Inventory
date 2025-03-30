from django.db import models
from authentication.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
# from django.apps import apps

# Unit=apps.get_model('employee','Unit')
# Employee=apps.get_model('employee','Employee')

# try:
#    admin.site.unregister(Unit)
# except NotRegistered:
#    pass
# Create your models here.
class Unit(models.Model):
   name=models.CharField("Name of the Unit",max_length=100)
   type = models.CharField(max_length=50, choices=[
        ('Civil', 'Civil'),
        ('Traffic', 'Traffic'),
        ('Armed Forces', 'Armed Forces'),
    ],
      default='Civil'    
    )

   def __str__(self):
      return self.name

# class Employee(CustomUser):
   
#    name=models.CharField("Name of the employee",max_length=50,null=True,blank=True)
#    # CustomUser_ptr = models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=1)
#    # age=models.IntegerField("Age of the employee")
#    # phone=models.IntegerField("Phone Number of the employee ")
#    # unit=models.ForeignKey(to=Unit,on_delete=models.CASCADE)
#    # designation=models.CharField("Designation of the employee",max_length=50)
#    # isHead=models.BooleanField("Is the head of the Unit?")

