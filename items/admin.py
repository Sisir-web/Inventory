from django.contrib import admin
from .models import Item_category
from .models import Item
from .models import Item_unit_mapping
# Register your models here.

@admin.register(Item_category)
class Itemcategory(admin.ModelAdmin):
   pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  pass

@admin.register(Item_unit_mapping)
class mapping(admin.ModelAdmin):
   pass