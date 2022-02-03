from django.urls import path

from .views import GeoMapView

app_name = "geo"

urlpatterns = [
    path("map/", GeoMapView.as_view()),
]