from django.forms import ModelForm
from model.models import ApartmentBuilding, Apartment

class ApartmentBuildingForm(ModelForm):
    class Meta:
        model = ApartmentBuilding
        fields = ['address','admin','neighbourhood','lat','lng']

class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        field = ['name','price','description','area','image','building']
    