from django.contrib import admin
from .model.models import Apartment, UserProfile, Buyer, Admin, Post, ApartmentBuilding

admin.site.register(Apartment)
admin.site.register(UserProfile)
admin.site.register(Buyer)
admin.site.register(Admin)
admin.site.register(Post)
admin.site.register(ApartmentBuilding)
