from django.contrib.gis import admin
# On peut LeafletGeoAdmin par admin.OSMGeoAdmin
from .models import Borne, Region
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

# class IncidenceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location')
#
# admin.site.register(Incidence, IncidenceAdmin)

class BorneAdmin(LeafletGeoAdmin):
    # pass
    list_display = ('name', 'east', 'nord')
# Register your models here.

class RegionAdmin(LeafletGeoAdmin):
    list_display = ('nom', 'region')

admin.site.register(Borne,BorneAdmin)
admin.site.register(Region,RegionAdmin)
