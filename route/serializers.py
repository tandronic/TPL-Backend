from rest_framework import serializers

from route.models import Stop, Route, Ticket, Payments


class StopSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField()

    class Meta:
        model = Stop
        fields = ('name', 'point')

    def get_point(self, value):
        return value.location.geojson


class RouteSerializer(serializers.ModelSerializer):
    route = serializers.SerializerMethodField()

    class Meta:
        model = Route
        fields = ('name', 'bus', 'route')

    def get_route(self, value):
        return value.location.geojson


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
