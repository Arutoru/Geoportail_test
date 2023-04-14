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
    list_display = ('amodiataire', 'niu', 'rccm', 'duree_bail', 'tel', 'superficie', 'date_caution', 'date_fin', 'montant_caution', 'statut', 'remarque')
# Register your models here.

class IndexAdmin(LeafletGeoAdmin):
    list_display = ('amodiataire', 'conso_m3', 'prix_unit', 'mont_conso', 'entretien', 'mont_payer')

admin.site.register(Aot,AotAdmin)
admin.site.register(Index,IndexAdmin)
