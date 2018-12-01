from package_model import Package, Base_package, PackagesDb
from flask import request, jsonify

package_list = PackagesDb()
def find_by_city(packages):
    for package in packages:
        if package.location == "kampala":
            return package

    return None

class PackageController():
    
    def __init__(self):
        pass

    def create_package(self):
        data = request.get_json()
        color = data.get("color")
        length = data.get("length")
        description = data.get("description")
        weight = data.get("weight")
        location = data.get("location")
        destination = data.get("destination")

        #assuming validation is done!!!!!!!!!!!!!

        my_package = Package(Base_package(color, length, description), weight, location, destination)
        
        package_list.add_package(my_package)
        return jsonify({
            "message": "created", "data": my_package.to_json()
        })
    def delete_package(self, package):
        pass
    def get_package_by_location(self):
        pack = package_list.select(find_by_city)
        if pack is None:
            return "not found"
    
        return pack.to_json()
    
    def get_by_color():
        pass

    def update_package(self, package):
        pass

    