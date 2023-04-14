from django.urls import path
from . import views
from djgeojson.views import GeoJSONLayerView
from reporter.models import Aot, Index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    # path('', HomePageView.as_view(), name='home'),
    path('accounts/profile/', views.AotListView.as_view(), name='home'),
    path('', views.AotListView.as_view(), name='home'),
    path('aot_data/', GeoJSONLayerView.as_view(model=Aot, properties=('amodiataire', 'niu', 'rccm', 'duree_bail', 'tel', 'superficie', 'date_caution', 'date_fin', 'montant_caution', 'statut', 'remarque')), name='aot_data'),
    path('index_data/', GeoJSONLayerView.as_view(model=Index, properties=('amodiataire', 'conso_m3', 'prix_unit', 'mont_conso', 'entretien', 'mont_payer')), name='index_data')
    # path('borne_data/', GeoJSONLayerView.as_view(model=Borne, properties=('name','picture_url','east','nord')), name='borne_data'),
    # path('region_data/', GeoJSONLayerView.as_view(model=Region, properties=('nom', 'date', 'superficie')), name='region_data')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
