from django.shortcuts import render, redirect
from django.http import HttpResponse
import json, requests
from django.views.decorators.csrf import csrf_exempt
import random, string

# Create your views here.

## Page Display Views

###Display Explore Page
def explore(request):

   return render(request, 'exploreTrip.html')

###Display Departure Flights Page
def displayDepartureFlights(request):

   return render(request, 'displayDepartureFlights.html')

###Display Returning Flights Page
def displayReturningFlights(request):

   return render(request, 'displayReturningFlights.html')

###Display Selected Departing Flight Page
def displaySelectedDepartureFlight(request):

   return render(request, 'displaySelectedDepartingFlight.html')

###Display Selected Returning Flight Page
def displaySelectedReturningFlight(request):

   return render(request, 'displaySelectedReturningFlight.html')

###Display Itenary Page
def displayItenary(request):

   return render(request, 'displayItenary.html')

###Display Passanger Form Page
def displayPassengerPage(request):

   return render(request, 'displayPassengerPage.html')

###Display Flight Review Page
def reviewDetails(request):

   return render(request, 'reviewDetails.html')

###Display Booking Page
def bookingConfirmation(request):

   return render(request, 'bookingConfirmation.html')

#----------------------------------------------------------------------------------------------------------------------------#
## Data Processing Views

###Once the Explore Form is submitted
def submitexploreform(request):
  try:
    
    if request.method=="POST":

      tripD = str(request.POST.get('trip'))
      fromD = str(request.POST.get('from')) 
      toD = str(request.POST.get('to')) 
      departD = str(request.POST.get('startdate')) 
      returnD = str(request.POST.get('enddate')) 
      passangerD = str(request.POST.get('passanger'))
      
      #Storing this data in session for further use
      request.session['returnDate']=returnD
      request.session['passanger']=passangerD
      request.session['tripType']=tripD

      data = {

            'tripD':tripD,
            'fromD':fromD,
            'toD':toD,
            'departD':departD,
            'returnD': returnD

      }

      print(data)
      
      #Redirected if trip selected is ONEWAY
      if returnD == "":

       url = "/api/departureFlights/?trip={}&from={}&to={}&departure={}".format(tripD,fromD,toD,departD)
       return redirect(url)   
       
      #Redirected if trip selected is ROUNDTRIP
      else:

       url = "/api/departureFlights/?trip={}&from={}&to={}&departure={}&return={}".format(tripD,fromD,toD,departD,returnD)
       return redirect(url)
      
    return tripD
  
  except:
   pass


#----------------------------------------------------------#
###Once the suitable departing flight is selected
def submitdepartureform(request):
      

      if request.method=="GET":
       

       selectedFlightId = request.GET.get("flight_id")
       print("Slected flight id is = {}".format(selectedFlightId))

       url = "/api/selectedDepartureFlight/?flightId={}".format(selectedFlightId)

       #Storing this data in session for further use
       request.session['dFlightId'] = selectedFlightId

       return redirect(url)
 

#----------------------------------------------------------#
###Once the button to display Returning flights is clicked 
def submitreturnform(request):
  
  try:
    if request.method=="POST":

      #Getting To and From value from selected departing flight page(NOT RECOMMENDED)
      #Change to receive it using session variable
      fromD = request.POST.get('fromForm')
      toD = request.POST.get('toForm')


      returnDate = request.session['returnDate']
      
      data = {

            'fromD':fromD,
            'toD':toD,
            'returnDate':returnDate

      }

      url = "/api/returningFlights/?trip={}&from={}&to={}&return={}".format("ROUNDTRIP",fromD,toD,returnDate)

      return redirect(url)
  except:
   pass

#----------------------------------------------------------#
###Once the suitable returning flight is selected
def submitreturnselectedform(request):
      
      
      selectedReturnFlightId = request.GET.get("flight_id")
      print(selectedReturnFlightId)


      url = "/api/selectedReturningFlight/?flightId={}".format(selectedReturnFlightId)

      #Storing this data in session for further use
      request.session['rFlightId'] = selectedReturnFlightId

      return redirect(url)


#----------------------------------------------------------#
###Once the View Trip button is clicked
def submititenaryform(request):
  try:
    
    if request.method=="POST":

      #Retrieving session info
      returningFlight = request.session['rFlightId']
      departingFlight = request.session['dFlightId']
      passanger = request.session['passanger']
      tripType = request.session['tripType']
      

      data = {

            'departingFlight':departingFlight,
            'returningFlight':returningFlight

      }


      url = "/api/itenary/?trip={}&departingFlight={}&returningFlight={}&passanger={}".format(tripType,departingFlight,returningFlight,passanger)

      return redirect(url)
  except:
   pass
  
#----------------------------------------------------------#
###Once the Continue on View Trip Page button is clicked  
def submititenaryPage(request):
  try:
    
    if request.method=="POST":
      
      #Getting data from Itenary page
      tripData = request.POST.get("tripStr")
      tripId = request.POST.get("trip_id")
      print(tripData)
      print(tripId)

      #Storing Itenary data for further use
      request.session['tripInfo'] = tripData
      request.session['trip_id'] = tripId

      #Retrieving Passanger Count
      passanger = request.session['passanger']
      print(passanger)
      

      data = {
            'passanger':passanger,
      }

      url = "/api/passangerPage/?passanger={}".format(passanger)

      return redirect(url)
      
  except:
   pass
  
#----------------------------------------------------------#
###Once the trip data is successfully sent from Itenary page
def redirectPassangerPage(request):
      
   try:  
      passanger = request.session['passanger']
      print(passanger)
      

      data = {
            'passanger':passanger,
      }

      url = "/api/passangerPage/?passanger={}".format(passanger)
      return redirect(url)
   except:
    pass

  
#----------------------------------------------------------#
###Once the submit button is clicked on passanger page
def submitpassangerPage(request):

  if request.method=="POST":

   #Retrieving all info from passanger form
   fName = str(request.POST.get('firstName'))
   lName = str(request.POST.get('lastName')) 
   dob = str(request.POST.get('dob')) 

   # POST Request to create passanger API
   url = "http://localhost:8000/api/passangers/"
   header = {
    "Content-Type":"application/json"
    }
   payload ={
	"firstName": fName,  
	"lastName": lName,
	"dob": dob
   }
   result = requests.post(url,  data=json.dumps(payload), headers=header)
   result_json = result.json()

   #Retrieving passanger ID from response
   passangerId= result_json["id"]
   print(passangerId)

   # Storing passanger ID in session variable
   request.session['passanger_id'] = passangerId
   
   #Retrieving Trip Info TO be sent in URL
   tripD = request.session['tripInfo']

   pData = {

            "fName":fName,
            "lName":lName,
            "dob": dob

      }

   url = "/api/reviewDetails/?passanger={}&trip={}".format(pData, tripD)

   return redirect(url)
  

#----------------------------------------------------------#
###Once the Complete Booking is clicked on Review page
@csrf_exempt
def submitreviewform(request):
  
  try:
    if request.method=="POST":
    
    #---------CARD PROCESSING------------- 
      #Retrieving card data from card form
      cardName = str(request.POST.get('cname'))
      cardNumber = str(request.POST.get('ccnum')) 
      expmonth = str(request.POST.get('expmonth')) 
      expyear = str(request.POST.get('expyear')) 
      cvv = str(request.POST.get('cvv')) 
      
    # POST request to add card to database 
    url = "http://localhost:8000/api/cards/"
    header = {
      "Content-Type":"application/json"
     }
    payload ={
        "nameOnCard": cardName,
        "cardNumber": cardNumber,
        "expiryMonth": expmonth,
        "expiryYear": expyear,
        "cvv": cvv
     }
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    result_json = result.json()

    #Retreiving card Id from API response
    cardId= result_json["id"]

    #Storing card ID in session variable
    request.session['card_id'] = cardId

   #-------BOOKING PROCESSING-----
    
    #Fetch Trip Id
    trip_Id = request.session['trip_id']
  
    #Fetch Passanger Id
    passanger_Id = request.session['passanger_id']

    #Fetch Card Id
    card_Id = request.session['card_id']

    #Creating Random Booking Refernce Number
    brn= ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    bookingRefernceNumber=brn
    tripId=trip_Id
    passangerId= passanger_Id
    cardId = card_Id
    isMember= False
    contactEmail= "gurkirat2773@gmail.com"

    #POST request to add Booking to database
    url = "http://localhost:8000/api/bookings/"
    header = {
      "Content-Type":"application/json"
     }
    payload ={
        "bookingReferenceNumber": bookingRefernceNumber,
        "trip": tripId,
        "passanger": passangerId,
        "payment": cardId,
        "isMember": isMember,
        "contactEmail": contactEmail
     }
    
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    result_json = result.json()

    #Retrieving Booking Refernce Number from API response
    bookingId= result_json["bookingReferenceNumber"]

    url = "/api/bookingConfirmation/?bookingReferenceNumber={}".format(bookingId)

    return redirect(url)

  except:
    pass
  