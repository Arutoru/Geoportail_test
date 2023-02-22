from django.contrib.gis import admin
# On peut LeafletGeoAdmin par admin.OSMGeoAdmin
from .models import Aot
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

# class IncidenceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location')
#
# admin.site.register(Incidence, IncidenceAdmin)

class AotAdmin(LeafletGeoAdmin):
    # pass
    list_display = ('amodiatair', 'niu', 'rccm', 'duree_bail', 'tel', 'sup', 'date_caut', 'statut', 'remarque')
# Register your models here.


admin.site.register(Aot,AotAdmin)
