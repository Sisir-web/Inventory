from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import JsonResponse


def viewallunitforms(request):
   user=request.user
   print(user.email)
   if request.user.is_authenticated:
     return JsonResponse(data={'messg':'I am authenticate','user':user.email})

   return JsonResponse(data={'messg':'Not authenticated',})