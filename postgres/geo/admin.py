from django.contrib.gis import admin

from .models import Geo


@admin.register(Geo)
class GeoAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("name", "location")
