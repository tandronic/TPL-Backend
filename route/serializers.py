import json

from rest_framework import serializers

from route.models import Stop, Route, Ticket, Payments, Bus


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'name')


class StopSerializer(serializers.ModelSerializer):
    point = serializers.SerializerMethodField()
    bus = BusSerializer(many=True, read_only=True)

    class Meta:
        model = Stop
        fields = ('name', 'point', 'bus')

    def get_point(self, value):
        return json.loads(value.location.geojson)


class RouteSerializer(serializers.ModelSerializer):
    route = serializers.SerializerMethodField()
    bus = BusSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        fields = ('name', 'bus', 'route')

    def get_route(self, value):
        return json.loads(value.location.geojson)


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
