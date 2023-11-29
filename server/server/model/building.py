class Building:
    def __init__(apartments, address, name):
        self.apartments = apartments
        self.address = address
        self.name = name

    def get_apartments(self):
        return self.apartments
    
    def get_address(self):
        return self.address
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name