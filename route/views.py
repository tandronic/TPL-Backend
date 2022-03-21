from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from route.models import Stop, Route, Ticket, Payments
from route.serializers import StopSerializer, RouteSerializer, TicketsSerializer, PaymentsSerializer


class StopAPIView(ListAPIView):
    queryset = Stop.objects.all()
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = StopSerializer
    permission_classes = (IsAuthenticated,)


class BusRouteAPIView(ListAPIView):
    queryset = Route.objects.all()
    search_fields = ['name', 'bus']
    filter_backends = (filters.SearchFilter,)
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticated,)


class TicketsAPIView(ListAPIView):
    queryset = Ticket.objects.all()
    search_fields = ['type_of_ticket']
    filter_backends = (filters.SearchFilter,)
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)


class PaymentsAPIView(ListAPIView):
    queryset = Payments.objects.all()
    search_fields = ['type_of_ticket']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PaymentsSerializer
    permission_classes = (IsAuthenticated,)
