"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views.apartmentListView import ApartmentListCreateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import api

urlpatterns = [
    path('api/',include('account.url')),
    # path(
    #     "api/apartment/",
    #     ApartmentListCreateView.as_view(),
    #     name="apartment-list-create",
    # ),
    path('api/apartments/',api.apartment_list,name=''),
    path('api/apartments/<str:name>/', api.apartment_get, name='apartment-get'),
    path('api/apartments/<str:name>/image/', api.get_apartment_image, name='apartment-image'),
    path('api/add/building/',api.add_apartment_building,name='apartment-building-get'),
    path('api/add/apartment/',api.add_apartment,name='apartment-get'),
    path("admin/", admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)