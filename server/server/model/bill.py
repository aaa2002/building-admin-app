class Bill:
    def __init__(self, id, email, building, apartment, total, status, date):
        self.id = id
        self.email = email
        self.total = total
        self.status = status
        self.date = date

    def get_id(self):
        return self.id
    
    def get_email(self):
        return self.email
    
    def get_building(self):
        return self.building
    
    def get_apartment(self):
        return self.apartment
    
    def get_total(self):
        return self.total
    
    def get_status(self):
        return self.status
    
    def get_date(self):
        return self.date
    
    def set_total(self, new_total):
        self.total = new_total

    def set_status(self, new_status):
        self.status = new_status

    def set_date(self, new_date):
        self.date = new_date