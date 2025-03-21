from django.contrib.auth.models import User
from django.db import models
from employee.models import Unit

# Create your models here.
class CustomUser(User):
   age=models.IntegerField("Age of the employee")
   phone=models.IntegerField("Phone Number of the employee ",max_length=10,null=True,blank=True)
   unit=models.ForeignKey(to=Unit,on_delete=models.CASCADE)
   designation=models.CharField("Designation of the employee",max_length=50,null=True,blank=True)
   isHead=models.BooleanField("Is the head of the Unit?")
   
   def __str__(self):
      return self.username