import requests


def get_directions(source, destination):
    # serializer = LocationSerializer(data=data)
    source = construct_location(source)
    destination = construct_location(destination)
    parameters = {
        "api-version" : 1,
        "apikey" : "fb7ec0552c18c309f58d77cdae79357e42ec274375fc7548",
        "vehicle" : "car",
        "point": source,
        "point": destination
    }
    r = requests.get("https://maps.vietmap.vn/api/route")
    if r.status_code == 200:
        # return data
        return
    else :
        # raise exception
        return False 

def construct_location(location):
    result = ""
    result = str(location.geo_location_x) + "," + str(location.geo_location_y)
    return result