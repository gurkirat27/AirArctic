from rest_framework import serializers
from .models import Trip
from Flight.serializers import FlightSerializer
from Flight.models import Flight, Airport

class TripSerializer1(serializers.ModelSerializer):

    departingFlight = FlightSerializer(read_only = True)
    returningFlight = FlightSerializer(read_only = True)

    departingFlight_id = serializers.IntegerField(write_only = True)
    returningFlight_id = serializers.IntegerField(write_only = True)


    class Meta:
        model = Trip

        fields = ['departingFlight', 'departingFlight_id','returningFlight', 'returningFlight_id']

    #def get_trip_description(self, obj, departureAirport, destinationAirport):
     #    return departureAirport.iataCode + "TO" + destinationAirport.iataCode
        
     
            
class TripSerializer2(serializers.ModelSerializer):

    departingFlight = FlightSerializer(read_only = True)
    #returningFlight = FlightSerializer(read_only = True)

    departingFlight_id = serializers.IntegerField(write_only = True)
    #returningFlight_id = serializers.IntegerField(write_only = True)


    class Meta:
        model = Trip

        fields = ['departingFlight', 'departingFlight_id']