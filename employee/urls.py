from django.urls import path
from . import views


urlpatterns=[
   path("view/<str:id>/",views.view_employee),
   path("delete/<str:id>/",views.delete_employee),
   path("update/<str:id>)/",views.update_employee),
   path("create/",views.create_employee,name='create'),
   path("viewall/",views.viewall_employee),
   path("home/",views.home_employee,name='home'),
]