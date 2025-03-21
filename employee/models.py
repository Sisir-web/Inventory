from django.db import models

# Create your models here.
class Unit(models.Model):
   name=models.CharField("Name of the Unit",max_length=20)

   def __str__(self):
      return self.name

class Employee(models.Model):
   
   name=models.CharField("Name of the employee",max_length=50)
   age=models.IntegerField("Age of the employee")
   phone=models.IntegerField("Phone Number of the employee ")
   unit=models.ForeignKey(to=Unit,on_delete=models.CASCADE)
   designation=models.CharField("Designation of the employee",max_length=50)
   isHead=models.BooleanField("Is the head of the Unit?")
   
