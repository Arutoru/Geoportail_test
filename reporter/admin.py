from django.contrib.gis import admin
# On peut LeafletGeoAdmin par admin.OSMGeoAdmin
from .models import Aot, Index, Route
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

# class IncidenceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location')
#
# admin.site.register(Incidence, IncidenceAdmin)

class AotAdmin(LeafletGeoAdmin):
    # pass
    list_display = ('amodiataire', 'niu', 'rccm', 'duree_bail', 'tel', 'superficie', 'date_caution', 'date_fin', 'montant_caution', 'localisation', 'statut', 'remarque')
# Register your models here.

class IndexAdmin(LeafletGeoAdmin):
    list_display = ('amodiataire', 'conso_m3', 'prix_unit', 'mont_conso', 'entretien', 'mont_payer')

class RouteAdmin(LeafletGeoAdmin):
    list_display = ( 'nom_rue', 'type', 'numero_rue')

admin.site.register(Aot,AotAdmin)
admin.site.register(Index,IndexAdmin)
admin.site.register(Route,RouteAdmin)
