from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from route.models import Route, Stop


@admin.register(Stop)
class LandAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', )


@admin.register(Route)
class LandAdmin(LeafletGeoAdmin):
    list_display = ('name', 'bus', 'location')
    search_fields = ('name', 'bus')
