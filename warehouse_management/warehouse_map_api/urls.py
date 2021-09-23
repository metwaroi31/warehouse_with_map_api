from django.urls import path

from warehouse_map_api.views.warehouse import add_warehouse_view
from warehouse_map_api.views.staff import add_staff
urlpatterns = [
    path('api/add_warehouse', add_warehouse_view),
    path('api/add_staff', add_staff)
]
