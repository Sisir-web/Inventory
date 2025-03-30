from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import get_user_model,authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout

User=get_user_model()

# Create your views here.
def home(request):
   return render(request, "index.html")

def signup(request):

   if request.method == "POST":
      username = request.POST.get('username')
      fname = request.POST.get('fname')
      lname = request.POST.get('lname')
      mail = request.POST.get('email')
      pass1 = request.POST.get('password1')
      pass2 = request.POST.get('password2')

      if pass1 != pass2:
         messages.error(request, "Password Mismatch!")
         return redirect('home')

      myuser = User.objects.create_user(username=username,email=mail,password=pass1)
      myuser.first_name = fname
      myuser.last_name = lname
      myuser.save()

      messages.success(request, "Your Account has been successfully created.")

      return redirect('signin')
   
   return render(request, "signup.html")

def signin(request):

   if request.method == "POST":
      username = request.POST['username']
      pass1 = request.POST.get('pass1',"")

      user = authenticate(username=username, password=pass1)

      if user is not None:
         login(request, user)
         fname = user.first_name
         return render(request, "index.html", {'fname': fname})
      else:
         messages.error(request, "Bad Credentials!")
         return redirect('home')
   return render(request, "signin.html")

def signout(request):
   logout(request)
   messages.success(request, "Logged out Successfully")
   return redirect('home ')