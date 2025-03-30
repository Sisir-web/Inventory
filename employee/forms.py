from django import forms
from authentication.models import CustomUser

class AddEmployeeForm(forms.ModelForm):

   class Meta:
      model = CustomUser
      fields =("age","phone","department","unit","designation")
      widgets ={
               'age':forms.NumberInput(attrs={'class':'form-control'}),
               'phone':forms.NumberInput(attrs={'class':'form-control'}),
               'department':forms.TextInput(attrs={'class':'form-control'}),
               'unit':forms.TextInput(attrs={'class':'form-control'}),
               'designation':forms.TextInput(attrs={'class':'form-control'}),
               # 'isHead':forms.BooleanField(attrs={'class':'form-control'}),
       }