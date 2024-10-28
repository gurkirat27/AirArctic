
from django.urls import path, include
from . import views


urlpatterns = [

    path('trips/',views.retrieveAllTrips),

    # Fetch Passangers endpoints
    path('passangers/',views.retrieveAllPassanger),
    path('passanger/<int:id>',views.retrieveSinglePassanger),

    path('passangerForm/',views.addPassanger, name='passangerForm'),
    path('passangerView/',views.viewPassanger, name='passangerView'),

        # Card Details endpoints
    path('cards/',views.retrieveAllCards),
    path('card/<int:id>',views.retrieveSingleCard),

    path('cardForm/',views.addCard, name='cardForm'),
    path('cardView/',views.viewCards, name='cardView'),

    
        # Booking endpoints
    path('bookings/',views.retrieveAllBookings),
    path('booking/<int:id>',views.retrieveSingleBooking),

    path('bookingForm/',views.addBooking, name='bookingForm'),
    path('bookingView/',views.viewBookings, name='bookingView'),

]