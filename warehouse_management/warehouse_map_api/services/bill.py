from warehouse_map_api.serializers.bill import BillSerializer
from warehouse_map_api.models.bill import bill
from warehouse_map_api.models.bill_product import bill_product

def create_bill(data):
    serializer = BillSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
    return serializer.data

def get_bill(bill_id):
    bill_to_get = bill.objects.get(id=bill_id)
    serializer = BillSerializer(bill_to_get)

    return serializer.data

def delete_bill(bill_id):
    bill_to_delete = bill.objects.get(id=bill_id)
    bill_to_delete.delete()
    
    return True

def get_detail_bill(bill_id):
    bill_products_to_get = bill_product.objects.filter()
    return True
# not use
# def update_bill(data, bill_id):
#     bill_to_update = bill.objects.get(id=bill_id)
#     serializer = BillSerializer(bill_to_update, data)
#     if serializer.is_valid():
#         serializer.save()
#     return serializer.data

