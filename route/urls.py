from django.urls import path

from route.views import StopAPIView, BusRouteAPIView, TicketsAPIView, PaymentsAPIView


urlpatterns = [
    path('stop/', StopAPIView.as_view()),
    path('bus-route/', BusRouteAPIView.as_view()),
    path('tickets/', TicketsAPIView.as_view()),
    path('payments/', PaymentsAPIView.as_view()),
]
