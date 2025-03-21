from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUser:
   list_display=['age','phone','unit','designation','isHead']