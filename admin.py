from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from .models import ImageSpot, Barangay

admin.site.register(ImageSpot, LeafletGeoAdmin)
admin.site.register(Barangay, LeafletGeoAdmin)
