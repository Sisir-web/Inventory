from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ItemUnitMapping

@login_required
def item_unit_mapping_list(request):
    user_unit = request.user.unit  # Get the department of the logged-in employee
    item_mappings = ItemUnitMapping.objects.filter(unit=user_unit)  # Filter by department
    
    return render(request, 'items/item_unit_mapping_list.html', {'item_mappings': item_mappings})

