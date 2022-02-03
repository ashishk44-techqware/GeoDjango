from django.contrib.gis.db.models import PointField
from django.db import models


class Geo(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    location = PointField()
