from django.db import models
from Flight.models import Flight,Airport
#from AirArctic.Member.models import Member
# Create your models here.



class Trip(models.Model):

    TRIP_CHOICE = (
    ("ROUNDTRIP" , "Round Trip"),
    ("ONEWAY" , "One way"),
     )

    trip = models.CharField(max_length=15,choices=TRIP_CHOICE, default="ROUNDTRIP")
   # tripDescription = Flight.departureAirport + "TO" + Flight.destinationAirport
    #departingFlight = models.ForeignKey(Flight, on_delete=models.PROTECT, default=1, related_name = 'departingFlight')
    departingFlight = models.ForeignKey(Flight, on_delete=models.PROTECT, default=1, related_name = 'departingFlight')
    returningFlight = models.ForeignKey(Flight, on_delete=models.PROTECT, default=1, related_name = 'returningFlight')


    


