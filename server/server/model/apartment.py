class Apartment:
    def __init__(self, number, floor, building, rent):
        self.number = number
        self.floor = floor
        self.building = building
        self.rent = rent

    def get_number(self):
        return self.number
    
    def get_floor(self):
        return self.floor
    
    def get_building(self):
        return self.building
    
    def get_rent(self):
        return self.rent

    def set_rent(self, new_rent):
        self.rent = new_rent