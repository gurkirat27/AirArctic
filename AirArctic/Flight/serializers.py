from rest_framework import serializers
from .models import Airport, Aircraft, Flight

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['id', 'iataCode', 'airportName', 'airportLocation']

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'aircraftModel']

class FlightSerializer(serializers.HyperlinkedModelSerializer):


    departureAirport = AirportSerializer(read_only=True)
    destinationAirport = AirportSerializer(read_only=True)
    airCraft = AircraftSerializer(read_only=True)
    
    #designatedActivity = GymActivitySerializer(read_only=True)
    #designatedActivity_id = GymActivitySerializer(write_only=True)

    class Meta:
        model = Flight
        fields = ['id', 'flightNumber', 'airCraft', 'departureAirport', 'destinationAirport', 'departureDate', 'arrivalDate', 'departureTime', 'arrivalTime', 'seatsAvailableToBook' ]

    def calculateFlightTime():
        flightTime =  Flight.departureTime - Flight.arrivalTime
        return flightTime
        
