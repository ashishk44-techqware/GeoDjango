import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import Geo


class GeoMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"

    def get_context_data(self, **kwargs):
        """Return the view context data."""
        context = super().get_context_data(**kwargs)
        context["markers"] = json.loads(serialize("geojson", Geo.objects.all()))
        return context

        