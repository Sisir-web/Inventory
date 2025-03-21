from django import forms
from .models import Employee

class AddEmployeeForm(forms.ModelForm):

   class Meta:
      model = Employee
      fields =("name","age","phone","unit")
      widgets = {
         'name':forms.TextInput(attrs={'class':'form-control'}),
         'age':forms.NumberInput(attrs={'class':'form-control'}),
         'phone':forms.NumberInput(attrs={'class':'form-control'}),
         
      }