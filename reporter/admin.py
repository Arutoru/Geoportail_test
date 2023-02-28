from django.contrib.gis import admin
# On peut LeafletGeoAdmin par admin.OSMGeoAdmin
from .models import Aot, Index
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

class IndexAdmin(LeafletGeoAdmin):
    list_display = ('amodiatair', 'conso_m3', 'prix_unit', 'mont_conso', 'entretien', 'mont_payer')

admin.site.register(Aot,AotAdmin)
admin.site.register(Index,IndexAdmin)
