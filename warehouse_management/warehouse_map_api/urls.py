from django.urls import path

from warehouse_map_api.views.warehouse import add_warehouse_view, warehouse_view
from warehouse_map_api.views.staff import add_staff
urlpatterns = [
    # warehouse api
    path('api/add_warehouse', add_warehouse_view),
    path('api/warehouse/<int:id>', warehouse_view),

    path('api/add_staff', add_staff)
]
