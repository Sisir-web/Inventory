from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'unit', 'isHead', 'is_staff', 'is_superuser')
    list_filter = ('unit', 'isHead', 'is_staff', 'is_superuser')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Unit Information', {'fields': ('unit', 'isHead')}), 
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Unit Information', {'fields': ('unit', 'isHead')}),  
    )

    def get_queryset(self, request):
        """Filter users so that Unit Heads only see employees from their own unit."""
        qs = super().get_queryset(request)

        # Superusers see all employees
        if request.user.is_superuser:
            return qs
        
        # Unit Heads only see employees from their own unit
        if request.user.isHead:
            return qs.filter(unit=request.user.unit)

        return qs.none()  # Default: Hide all users if no permission

# Proper registration
admin.site.register(CustomUser, CustomUserAdmin)
