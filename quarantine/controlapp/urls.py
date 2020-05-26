
from django.conf.urls import include 
from .views import HomePageView, district_datasets
from django.urls import path
from djgeojson.views import GeoJSONLayerView
from .models import districts, Incidences

urlpatterns= [
    path('', HomePageView.as_view(), name = 'home'),
    path('district_data/', GeoJSONLayerView.as_view(model=districts, properties=('district','zone','area','division')), name = 'district'),
    #path('district_data/', district_datasets , name="district"),
    path('incidence_data/', GeoJSONLayerView.as_view(model=Incidences, properties=('name','geom')), name = 'incidence'),
]