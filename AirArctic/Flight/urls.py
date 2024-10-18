
from django.urls import path, include
from . import views


urlpatterns = [

    # Fetch Flight endpoints
    path('flights/',views.retrieveAllFlights),
    path('flight/<int:id>',views.retrieveSingleFlight),

    # Fetch Airport endpoints
    path('airports/',views.retrieveAllAirports),
    path('airport/<int:id>',views.retrieveSingleAirport),

    # Fetch Aircraft endpoints
    path('aircrafts/',views.retrieveAllAircrats),
    path('aircraft/<int:id>',views.retrieveSingleAircraft),

    #Web interface endpoints
    path('airportList/',views.airportView, name='airportView'),
    path('airportForm/',views.addAirport, name='airportForm'),
    path('aircraftList/',views.aircraftView, name='aircraftView'),
    path('aircraftForm/',views.addAircraft, name='aircraftForm'),
    path('flightForm/',views.addFlight, name='flightForm'),
    path('flightDisplay/',views.flightView, name='flightsView'),

    #Index

    path('index/',views.index),
   # path('explore/',views.explore),
   # path('departureFlights/',views.displayDepartureFlights, name='displayDepartureFlights'),
]