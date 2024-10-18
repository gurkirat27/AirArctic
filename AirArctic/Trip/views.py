from django.shortcuts import render
from django.db import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trip
from Flight.models import Flight
from .serializers import TripSerializer1, TripSerializer2
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def retrieveAllTrips(request):

    if request.method == 'GET':
        trips = Trip.objects.all()
        serialized_item = TripSerializer1(trips, many=True)

        return Response(serialized_item.data)

    if request.method == 'POST':
       
       '''
       
       #Departing & returning Flight Id sent in the URL by client app
       #http://127.0.0.1:8000/api/trips/?trip=roundtrip&departingFlightId ={flight.FlightId}&returningFlightId ={flight.FlightId}
       trip_type = request.query_params.get('trip')
       departing_flight_id = request.query_params.get('departingFlightId')
       returning_flight_id = request.query_params.get('returningFlightId')

       #Condition to check if roundtrip has both returningFlightId & departing flight Id

       #if trip_type =="Roundtrip":
         
       if departing_flight_id and returning_flight_id:

            flights = Flight.objects.all()
            

            #Condition to fetch flight objects using ID's

            departingFlightObj = flights.filter(id = departing_flight_id)
            returningFlightObj = flights.filter(id = returning_flight_id)

            Trip.trip = trip_type
            Trip.departingFlight = departingFlightObj
            Trip.returningFlight = returningFlightObj

            trip = Trip.save()

            
            serialized_item = TripSerializer(trip)
            #serialized_item.is_valid(raise_exception=True)
            #serialized_item.save()
    return Response(serialized_item.data, status.HTTP_201_CREATED)

    
           ''' 
       
    trip = request.query_params.get('trip')


    if trip == 'ROUNDTRIP':

           
     serialized_item = TripSerializer1(data = request.data)

     serialized_item.is_valid(raise_exception=True)

     serialized_item.save()
            
     return Response(serialized_item.data, status.HTTP_201_CREATED )

    elif trip == 'ONEWAY':
      
      Trip.departingFlight_id == None   
       
      serialized_item = TripSerializer2(data = request.data)

      serialized_item.is_valid(raise_exception=True)

      serialized_item.save()
            
      return Response(serialized_item.data, status.HTTP_201_CREATED )
    

 