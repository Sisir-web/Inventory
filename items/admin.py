from django.contrib import admin
from authentication.models import CustomUser
from .models import Item_category, Item, Item_unit_mapping

# Register Item Category
@admin.register(Item_category)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Assuming 'name' exists in Item_category

# Register Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')  # Assuming 'name' & 'category' exist in Item

# Register Item-Unit Mapping
@admin.register(Item_unit_mapping)
class ItemUnitMappingAdmin(admin.ModelAdmin):
    list_display = ('item', 'unit', 'quantity')  # Display relevant fields
    list_filter = ('unit',)  # Filter by unit for better usability

    def get_queryset(self, request):
        """Filter items based on the logged-in user's unit."""
        qs = super().get_queryset(request)

        # Superuser can see all items
        if request.user.is_superuser:
            return qs 

        # Unit Heads only see items assigned to their own unit
        if getattr(request.user, 'isHead', False):  
            return qs.filter(unit=request.user.unit)
        
        return qs.none()  # Hide everything for unauthorized users
