from django.db import models
from employee.models import Employee,Unit
from items.models import Item

# Create your models here.
class RequestForm(models.Model):
   name=models.ForeignKey(to=Employee,on_delete=models.CASCADE)
   unit=models.ForeignKey(to=Unit,on_delete=models.CASCADE)
   item=models.ForeignKey(to=Item,on_delete=models.CASCADE)
   quantity=models.IntegerField("Enter the quantity")
   daterequsition=models.IntegerField("Date requisition")
   datecompletion=models.IntegerField("Date completion")
   status=models.CharField("Status of request")


   