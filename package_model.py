class Base_package(object):

    def __init__(self, color, length, description):
        self.color = color
        self.length = length
        self.description = description

class Package(object):
    def __init__(self, base_package, weight, location, destination):
        # self.package_id = 0
        self.base_package = base_package
        self.weight = weight
        self.location = location
        self.destination = destination

    def to_json(self):
        return {"weight": self.weight,
                "location": self.location,
                "destination": self.destination,
                "color": self.base_package.color
                # "pack": self.base_package
                
        }

    @staticmethod
    def weight_in_pounds(weight_in_kg):
        return weight_in_kg * 1.23

class PackagesDb():
    def __init__(self):
        self.packages_list = []

    def add_package(self, package):
        self.packages_list.append(package)

    def get_package_by_id(self, package_id):
        for package in self.packages_list:
            if package.package_id == package_id:
                return package
        return None
    
    def get_packages(self):
        return self.packages_list

    def get_packages_json(self):
        return [package.to_json for package in self.packages_list]

    def select(self, func):
        return func(self.packages_list)