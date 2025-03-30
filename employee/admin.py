from django.contrib.admin import AdminSite, ModelAdmin
from django.contrib import admin
from .models import Unit
from django.contrib.admin.sites import NotRegistered
# from django.apps import apps



# def get_unit_model():
#     return apps.get_model('employee','models','Unit')

# def get_employee_model():
#     return apps.get_model('employee','models','Employee')

class UnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.groups.filter(name="Civil Admins").exists():
            return qs.filter(type="Civil")
        elif request.user.groups.filter(name="Traffic Admins").exists():
            return qs.filter(type="Traffic")
        elif request.user.groups.filter(name="Armed Forces Admins").exists():
            return qs.filter(type="Armed Forces")
        return qs.none()  # Hide everything for unauthorized users

# admin.site.register(get_unit_model(), UnitAdmin)

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'unit', 'designation']
#     list_filter = ['unit']
    
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         elif request.user.groups.filter(name="Civil Admins").exists():
#             return qs.filter(unit__type="Civil")
#         elif request.user.groups.filter(name="Traffic Admins").exists():
#             return qs.filter(unit__type="Traffic")
#         elif request.user.groups.filter(name="Armed Forces Admins").exists():
#             return qs.filter(unit__type="Armed Forces")
#         return qs.none()  # Hide everything for unauthorized users

#     def has_add_permission(self, request):
#         if request.user.is_superuser:
#             return True
#         return request.user.groups.filter(name__in=["Civil Admins", "Traffic Admins", "Armed Forces Admins"]).exists()

#     def has_change_permission(self, request, obj=None):
#         if request.user.is_superuser:
#             return True
#         if obj and request.user.groups.filter(name="Civil Admins").exists():
#             return obj.unit.type == "Civil"
#         if obj and request.user.groups.filter(name="Traffic Admins").exists():
#             return obj.unit.type == "Traffic"
#         if obj and request.user.groups.filter(name="Armed Forces Admins").exists():
#             return obj.unit.type == "Armed Forces"
#         return False

# # Custom Admin for Civil
# class CivilAdminSite(AdminSite):
#     site_header = "Civil Admin"
#     site_title = "Civil Administration"
#     index_title = "Welcome to Civil Admin Panel"

# civil_admin_site = CivilAdminSite(name='civil_admin')
# civil_admin_site.register(Employee)
# civil_admin_site.register(Unit)

# # Custom Admin for Traffic
# class TrafficAdminSite(AdminSite):
#     site_header = "Traffic Admin"
#     site_title = "Traffic Administration"
#     index_title = "Welcome to Traffic Admin Panel"

# traffic_admin_site = TrafficAdminSite(name='traffic_admin')
# traffic_admin_site.register(Employee)
# traffic_admin_site.register(Unit)

# # Custom Admin for Armed Forces
# class ArmedAdminSite(AdminSite):
#     site_header = "Armed Forces Admin"
#     site_title = "Armed Forces Administration"
#     index_title = "Welcome to Armed Forces Admin Panel"

# armed_admin_site = ArmedAdminSite(name='armed_admin')
# armed_admin_site.register(Employee)
# armed_admin_site.register(Unit)

# # Register models with respective admin sites
# # civil_admin_site.register(Employee)
# # traffic_admin_site.register(Employee)
# # armed_forces_admin_site.register(Employee)
# # Default Django admin registration for Employee (if needed)
# admin.site.register(Employee)