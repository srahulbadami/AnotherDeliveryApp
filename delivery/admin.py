from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis import admin

# Register your models here.

from .models import Delivery_Agent,User	,Customer,Delivery

admin.site.register(Delivery_Agent,admin.GeoModelAdmin)
admin.site.register(User)
admin.site.register(Customer,admin.GeoModelAdmin)
admin.site.register(Delivery,admin.GeoModelAdmin)

