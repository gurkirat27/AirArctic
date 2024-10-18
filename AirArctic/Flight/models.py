from django.db import models

# Create your models here.

class Airport(models.Model):

    iataCode = models.CharField(max_length=3)
    airportName = models.CharField(max_length=100)
    airportLocation = models.CharField(max_length=100)

    def __str__(self)-> str:
        return self.airportName

class Aircraft(models.Model):
    
    aircraftModel = models.CharField(max_length=100)

    def __str__(self)-> str:
        return self.aircraftModel

class Flight(models.Model):

    flightNumber = models.CharField(max_length=100)
    airCraft = models.ForeignKey(Aircraft, on_delete=models.PROTECT, default=1, related_name = 'departureAirport')
    departureAirport = models.ForeignKey(Airport, on_delete=models.PROTECT, default=1, related_name = 'destinationAirport')
    destinationAirport = models.ForeignKey(Airport, on_delete=models.PROTECT, default=1)
    departureDate = models.DateField()
    arrivalDate = models.DateField()
    departureTime = models.TimeField()
    arrivalTime = models.TimeField()
    seatsAvailableToBook = models.IntegerField()

    def __str__(self)-> str:
        return self.flightNumber
    