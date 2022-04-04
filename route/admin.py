from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from route.models import Route, Stop, Ticket, Payments, Bus


@admin.register(Stop)
class StopAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location', 'created_date')
    search_fields = ('name', 'bus__name')


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')
    search_fields = ('name',)


@admin.register(Route)
class RouteAdmin(LeafletGeoAdmin):
    list_display = ('name', 'created_date')
    search_fields = ('name', 'bus__name')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('type_of_ticket', 'price')
    search_fields = ('type_of_ticket',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'ticket', 'date', 'subscription', 'start_subscription',
                    'end_subscription')
    search_fields = ('user__email', 'ticket__type_of_ticket')
    list_filter = ('date', 'subscription', 'start_subscription', 'end_subscription')
