from django.db import models
from django.contrib.auth.models import User
from enum import IntEnum    
import uuid


class ApartmentBuilding(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    address = models.CharField(max_length=255, null=True)
    admin = models.CharField(max_length=255, null=True) # make a table later
    neighbourhood = models.CharField(max_length=255)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    
    class Meta:
         app_label = 'server'

    def __str__(self):
         return self.address

class Apartment(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,null=True)
    price = models.PositiveBigIntegerField(null=True)
    description= models.TextField(blank=True,null=True)
    area = models.FloatField(null=True)
    image = models.ImageField(upload_to="apartment_images/",null=True, blank=True)
    building=models.ForeignKey(ApartmentBuilding, on_delete=models.CASCADE)
    
    class Meta:
         app_label = 'server'

    def __str__(self):
         return self.name
    

# class UserRole(IntEnum):
#     ADMIN = 1
#     USER = 2

# class UserProfile(models.Model):
#     #user = models.OneToOneField(User, on_delete=models.CASCADE)
#     roles = models.JSONField(blank=True, null=True) # NEED TO BE DECODED
#     legal_name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     chat_id = models.CharField(max_length=255)  # not final

#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return self.legal_name

# class Buyer(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, default=None)
#     apartments = set()

#     def get_apartments(self):
#         return self.apartments
    
#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return self.user_profile.legal_name
    
# class Admin(models.Model):
#     user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, default=None)
    
#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return self.user_profile.legal_name
    
# class ApartmentBuilding(models.Model):
    
#     id = models.CharField(max_length=255,primary_key=True)
#     address = models.CharField(max_length=255)
#     admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
#     neighbourhood = models.CharField(max_length=255) 
    
#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return self.id

# class Post(models.Model):
#     apartment=apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)    
#     description=models.CharField(max_length=255)
#     poster =  models.ForeignKey(Admin, on_delete=models.CASCADE)    
#     imgUrl = models.CharField(max_length=255)
#     post_date = models.DateField()
#     price = models.FloatField()
#     #locationData  
