from django.urls import path
from rest_framework.decorators import schema
from warehouse_map_api.views.user import user_view

from warehouse_map_api.views.warehouse import add_warehouse_view, warehouse_view
from warehouse_map_api.views.staff import add_staff
from warehouse_map_api.views.user import add_user
from rest_framework_swagger.views import get_swagger_view

schema_view=get_swagger_view(title='Swagger')


urlpatterns = [
    # warehouse api
    path('api/add_warehouse', add_warehouse_view),
    path('api/warehouse/<int:id>', warehouse_view),

    path('api/add_staff', add_staff),
    path('api/add_user', add_user),
    path('api/user/<int:id>',user_view),
    path('', schema_view),
]
