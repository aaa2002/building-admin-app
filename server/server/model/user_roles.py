from enum import Enum

class UserRole(Enum):
    admin = 'ADMIN'
    tenant = 'TENANT'
    worker = 'WORKER'
