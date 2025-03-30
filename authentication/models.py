
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


# Custom Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
         user.set_password(password)
         user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


# Create your models here.
class CustomUser(AbstractUser):
   #The fields are not being reflected
   age=models.IntegerField("Age of the employee",null=True,blank=True)
   phone=models.IntegerField("Phone Number of the employee ",null=True,blank=True)
   department=models.CharField("Enter the Department ",max_length=10,null=True,blank=True)
   unit=models.ForeignKey('employee.Unit',on_delete=models.CASCADE,null=True,blank=True)
   designation=models.CharField("Designation of the employee",max_length=50,null=True,blank=True)
   isHead=models.BooleanField("Is the head of the Unit?",default=False)

def save(self, *args, **kwargs):
        """Automatically set is_staff=True if the user is a unit head."""
        if self.ishead:
            self.is_staff = True  # Unit heads get staff access
        super().save(*args, **kwargs)

objects = CustomUserManager()
   
def __str__(self):
      return self.username
   
   # def get_unit(self):
   #    """Using dynamic import to avoid the circular import"""
   #    Unit=apps.get_model('employee','Unit') #Dynamically getting the Unit model

   #    return Unit.objects.filter(CustomUser=self).first()#adjust based on relation.