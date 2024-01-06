from django.db import models
from django.contrib.auth.models import User
from enum import IntEnum    

class Apartment(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    address = models.CharField(max_length=255)
    building = models.ForeignKey('ApartmentBuilding',on_delete=models.CASCADE)
    area = models.FloatField()
    
    class Meta:
         app_label = 'server'

    def __str__(self):
         return self.id

class UserRole(IntEnum):
    ADMIN = 1
    USER = 2

class UserProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.JSONField(blank=True, null=True) # NEED TO BE DECODED
    legal_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255)  # not final

    class Meta:
        app_label = 'server'

    def __str__(self):
        return self.legal_name

class Buyer(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, default=None)
    apartments = set()

    def get_apartments(self):
        return self.apartments
    
    class Meta:
        app_label = 'server'

    def __str__(self):
        return self.user_profile.legal_name
    
class Admin(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, default=None)
    
    class Meta:
        app_label = 'server'

    def __str__(self):
        return self.user_profile.legal_name
    
class ApartmentBuilding(models.Model):
    
    id = models.CharField(max_length=255,primary_key=True)
    address = models.CharField(max_length=255)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    neighbourhood = models.CharField(max_length=255) 
    
    class Meta:
        app_label = 'server'

    def __str__(self):
        return self.id

class Post(models.Model):
    apartment=apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)    
    description=models.CharField(max_length=255)
    poster =  models.ForeignKey(Admin, on_delete=models.CASCADE)    
    imgUrl = models.CharField(max_length=255)
    post_date = models.DateField()
    price = models.FloatField()
    #locationData  


# class PropertyType(models.Model):
#     name = models.CharField(max_length=255)

#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return self.name

# class Amenity(models.Model):
#     name = models.CharField(max_length=255)

#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return self.name

# class Accommodation(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
#     amenities = models.ManyToManyField(Amenity)
#     host = models.ForeignKey(User, on_delete=models.CASCADE)
#     price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
#     address = models.TextField()

#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return self.title

# class Reservation(models.Model):
#     guest = models.ForeignKey(User, on_delete=models.CASCADE)
#     accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#     guests_count = models.PositiveIntegerField()

#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return f"{self.guest.username} - {self.accommodation.title} - {self.check_in_date} to {self.check_out_date}"

# class Review(models.Model):
#     guest = models.ForeignKey(User, on_delete=models.CASCADE)
#     accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField()

#     class Meta:
#         app_label = 'server'

#     def __str__(self):
#         return f"{self.guest.username} - {self.accommodation.title} - Rating: {self.rating}"
