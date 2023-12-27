from django.db import models
from django.contrib.auth.models import User

class PropertyType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'server'

    def __str__(self):
        return self.name

class Amenity(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = 'server'

    def __str__(self):
        return self.name

class Accommodation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()

    class Meta:
        app_label = 'server'

    def __str__(self):
        return self.title

class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guests_count = models.PositiveIntegerField()

    class Meta:
        app_label = 'server'

    def __str__(self):
        return f"{self.guest.username} - {self.accommodation.title} - {self.check_in_date} to {self.check_out_date}"

class Review(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta:
        app_label = 'server'

    def __str__(self):
        return f"{self.guest.username} - {self.accommodation.title} - Rating: {self.rating}"
