from rest_framework import serializers
from .models import Trip, Passengers, CardDetails, Booking
from Flight.serializers import FlightSerializer
from Flight.models import Flight, Airport

class TripSerializer1(serializers.ModelSerializer):

    departingFlight = FlightSerializer(read_only = True)
    returningFlight = FlightSerializer(read_only = True)

    departingFlight_id = serializers.IntegerField(write_only = True)
    returningFlight_id = serializers.IntegerField(write_only = True)


    class Meta:
        model = Trip

        fields = ['id','departingFlight', 'departingFlight_id','returningFlight', 'returningFlight_id']

    #def get_trip_description(self, obj, departureAirport, destinationAirport):
     #    return departureAirport.iataCode + "TO" + destinationAirport.iataCode
        
     
            
class TripSerializer2(serializers.ModelSerializer):

    departingFlight = FlightSerializer(read_only = True)
    #returningFlight = FlightSerializer(read_only = True)

    departingFlight_id = serializers.IntegerField(write_only = True)
    #returningFlight_id = serializers.IntegerField(write_only = True)


    class Meta:
        model = Trip

        fields = ['id','departingFlight', 'departingFlight_id']



class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ['id', 'firstName', 'lastName', 'dob']

class CardDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDetails
        fields = ['id', 'nameOnCard', 'cardNumber', 'expiryMonth', 'expiryYear', 'cvv']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['bookingReferenceNumber', 'trip', 'passanger', 'payment','isMember', 'contactEmail']