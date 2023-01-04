from django.urls import path
from .views import HomePageView
from djgeojson.views import GeoJSONLayerView
from reporter.models import Region, Borne
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('', HomePageView.as_view(), name='home'),
    path('accounts/profile/', HomePageView.as_view(), name='home'),
    path('borne_data/', GeoJSONLayerView.as_view(model=Borne, properties=('name','picture_url','east','nord')), name='borne_data'),
    path('region_data/', GeoJSONLayerView.as_view(model=Region, properties=('nom', 'date', 'superficie')), name='region_data')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
