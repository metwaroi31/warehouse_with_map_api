from warehouse_map_api.serializers.bill import BillSerializer
from warehouse_map_api.models.bill import bill
from warehouse_map_api.models.bill_product import bill_product
from warehouse_map_api.serializers.product import ProductSerializer

def create_bill(data):
    # print (data)
    bill_serializer = BillSerializer(data=data)
    
    if bill_serializer.is_valid():
        bill_serializer.save()
    detail_bill = get_detail_bill(bill_serializer.data["id"])
    return_bill = bill_serializer.data
    return_bill["products"] = detail_bill
    return return_bill

def get_bill(bill_id):
    bill_to_get = bill.objects.get(id=bill_id)
    detail_bill = get_detail_bill(bill_id)
    serializer = BillSerializer(bill_to_get)
    return_bill = serializer.data
    return_bill["products"] = detail_bill
    return return_bill

def delete_bill(bill_id):
    bill_to_delete = bill.objects.get(id=bill_id)
    bill_to_delete.delete()
    
    return True

def get_detail_bill(bill_id):
    return_detail_bill = []
    bill_products_to_get = bill_product.objects.filter(bill=bill_id)
    raw_bill_products = list(bill_products_to_get)
    
    for bill_detail in raw_bill_products:
        # get product serializer
        custom_JSON = {}
        custom_JSON["product"] = bill_detail.product.__dict__
        custom_JSON
        serializer = ProductSerializer(bill_detail.product)
        return_detail_bill.append(serializer.data)
    return return_detail_bill 
