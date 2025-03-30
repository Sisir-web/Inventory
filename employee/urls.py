from django.urls import path
from . import views
# from .admin import civil_admin_site, traffic_admin_site, armed_admin_site
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test

# Function to check if a user belongs to a specific group
# def is_civil_admin(user):
#     return user.is_superuser or user.groups.filter(name="Civil Admins").exists()

# def is_traffic_admin(user):
#     return user.is_superuser or user.groups.filter(name="Traffic Admins").exists()

# def is_armed_forces_admin(user):
#     return user.is_superuser or user.groups.filter(name="Armed Forces Admins").exists()

urlpatterns=[
   path("view/<str:id>/",views.view_employee),
   path("delete/<str:id>/",views.delete_employee),
   path("update/<str:id>)/",views.update_employee),
   path("create/",views.create_employee,name='create'),
   path("viewall/",views.viewall_employee),
   path("home/",views.home_employee,name='home'),
   # path('admin/civil', civil_admin_site.urls),
   # path('traffic-admin/traffic', traffic_admin_site.urls),
   # path('admin/armed', armed_admin_site.urls),
]



