from django.db import models
from employee.models import Unit

# Create your models here.

class Item_category(models.Model):
   """ It stores the item based on their category"""
   name=models.CharField("Name of the Category",max_length=50)

   def __str__(self):
      return self.name


class Item(models.Model):
   """It stores the item """
   name=models.CharField("Name of the Items",max_length=50)
   quantity=models.IntegerField("Quantity of the Items")
   category=models.ForeignKey(to=Item_category, on_delete=models.CASCADE)

   def __str__(self):
      return f'{self.name}={self.quantity}'

class Item_unit_mapping(models.Model):
   """Stores the item based on unit(allocated items to a unit)"""
   unit=models.ForeignKey(to=Unit,on_delete=models.CASCADE)
   item=models.ForeignKey(to=Item,on_delete=models.CASCADE)
   quantity=models.IntegerField("Quantity of the items for the unit")

   def __str__(self):
      return f'{self.unit}={self.quantity}/{self.item.quantity} {self.item.name}'
