from django.urls import path
from warehouse_map_api.views.warehouse import add_warehouse_view, warehouse_view
from warehouse_map_api.views.staff import add_staff, staff_view
from warehouse_map_api.views.user import add_user, user_view
from warehouse_map_api.views.product import *
from warehouse_map_api.views.position import add_position,position_view
from warehouse_map_api.views.bill import *
from rest_framework_swagger.views import get_swagger_view
from warehouse_map_api.views.order import add_order, order_view


urlpatterns = [
    # warehouse api
    path('api/add_warehouse', add_warehouse_view),
    path('api/warehouse/<int:id>', warehouse_view),

    # bill api
    path('api/add_bill', add_bill),
    path('api/bill/<int:id>', bill_view),

    # product api
    path('api/add_product', add_product),
    path('api/product/<int:id>', product_view),

    # staff api
    path('api/add_staff', add_staff),
    path('api/staff/<int:id>',staff_view),

    # user api
    path('api/add_user', add_user),
    path('api/user/<int:id>',user_view),

    # position api
    path('api/add_position', add_position),
    path('api/position/<int:id>',position_view),

    # order api
    path('api/add_order', add_order),
    path('api/order/<int:id>',order_view),

]
