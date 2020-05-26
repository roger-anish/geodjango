from django.contrib import admin
from .models import Incidences, districts
from leaflet.admin import LeafletGeoAdmin 
#from leaflet.forms.fields import PointField 

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    #pass
    list_display=('name','geom')

class districtsAdmin(LeafletGeoAdmin):
    #pass
    list_display=('district','area')

admin.site.register(Incidences,IncidencesAdmin)

admin.site.register(districts, districtsAdmin )   