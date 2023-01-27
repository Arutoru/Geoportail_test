from django.urls import path
from . import views
from djgeojson.views import GeoJSONLayerView
from reporter.models import Aot
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    # path('', HomePageView.as_view(), name='home'),
    path('accounts/profile/', views.AotListView.as_view(), name='home'),
    path('', views.AotListView.as_view(), name='home'),
    path('aot_data/', GeoJSONLayerView.as_view(model=Aot, properties=('amodiatair', 'niu', 'sup', 'date_caut')), name='aot_data')
    # path('borne_data/', GeoJSONLayerView.as_view(model=Borne, properties=('name','picture_url','east','nord')), name='borne_data'),
    # path('region_data/', GeoJSONLayerView.as_view(model=Region, properties=('nom', 'date', 'superficie')), name='region_data')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
