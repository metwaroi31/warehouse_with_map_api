from django.urls import path
from warehouse_map_api.views.position import add_position

from warehouse_map_api.views.warehouse import add_warehouse_view, warehouse_view
from warehouse_map_api.views.staff import add_staff, staff_view
from warehouse_map_api.views.user import add_user, user_view
from warehouse_map_api.views.position import add_position,position_view



urlpatterns = [
    # warehouse api
    path('api/add_warehouse', add_warehouse_view),
    path('api/warehouse/<int:id>', warehouse_view),

    path('api/add_staff', add_staff),
    path('api/staff/<int:id>',staff_view),

    path('api/add_user', add_user),
    path('api/user/<int:id>',user_view),

    path('api/add_position', add_position),
    path('api/position/<int:id>',position_view),

    

]
