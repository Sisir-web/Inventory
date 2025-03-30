from django.urls import path
from .views import item_unit_mapping_list

urlpatterns = [
    path('unit-items/', item_unit_mapping_list, name='unit_items'),
]
