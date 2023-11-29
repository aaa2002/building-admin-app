class Repair:
    def __init__(self, id, building, apartment, worker, repair_type, date, cost, status):
        self.id = id
        self.building = building
        self.apartment = apartment
        self.worker = worker
        self.repair_type = repair_type
        self.date = date
        self.cost = cost
        self.status = status

    def get_id(self):
        return self.id
    
    def get_building(self):
        return self.building
    
    def get_apartment(self):
        return self.apartment
    
    def get_worker(self):
        return self.worker
    
    def get_repair_type(self):
        return self.repair_type
    
    def get_date(self):
        return self.date
    
    def get_cost(self):
        return self.cost
    
    def get_status(self):
        return self.status
    
    def set_cost(self, new_cost):
        self.cost = new_cost

    def set_status(self, new_status):
        self.status = new_status

    def set_date(self, new_date):
        self.date = new_date

    def serialize(self):
        return {
            'id': self.id,
            'building': self.building,
            'apartment': self.apartment,
            'worker': self.worker,
            'repair_type': self.repair_type,
            'date': self.date,
            'cost': self.cost,
            'status': self.status
        }