
from django.urls import path, include
from . import views


urlpatterns = [

   
    path('exploreTrip/',views.explore),
    path('departureFlights/',views.displayDepartureFlights, name='displayDepartureFlights'),
    path('returningFlights/',views.displayReturningFlights, name='displayReturningFlights'),
    path('submitForm/',views.submitexploreform, name='submitexploreform'),
    path('submitdepartureForm/',views.submitdepartureform, name='submitdepartureform'),
    path('submitreturnForm/',views.submitreturnform, name='submitreturnform'),
    path('submitreturnselectedForm/',views.submitreturnselectedform, name='submitreturnselectedform'), 
    path('selectedDepartureFlight/',views.displaySelectedDepartureFlight, name='displaySelectedDepartureFlight'),
    path('selectedReturningFlight/',views.displaySelectedReturningFlight, name='displaySelectedReturningFlight'),
    path('itenary/',views.displayItenary, name='displayItenary'),
    path('submititenaryform/',views.submititenaryform, name='submititenaryform'),
    path('passangerPage/',views.displayPassengerPage, name='displayPassengerPage'),
    path('submititenaryPage/',views.submititenaryPage, name='submititenaryPage'),
    path('reviewDetails/',views.reviewDetails, name='reviewDetails'),
    path('redirectPassangerPage/',views.redirectPassangerPage, name='redirectPassangerPage'),
    path('submitpassangerPage/',views.submitpassangerPage, name='submitpassangerPage'),
    path('submitreviewform/',views.submitreviewform, name='submitreviewform'),
    path('bookingConfirmation/',views.bookingConfirmation, name='bookingConfirmation'),
    
]