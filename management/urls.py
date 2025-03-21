from django.urls import path
from . import views
urlpatterns=[
   path('viewAll/',views.viewallunitforms,name='viewAllRequestForms')
]