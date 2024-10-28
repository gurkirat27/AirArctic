from django.shortcuts import render, redirect
from django.http import HttpResponse
import json, requests
from django.views.decorators.csrf import csrf_exempt
import random, string

# Create your views here.

def explore(request):

   return render(request, 'exploreTrip.html')

def displayDepartureFlights(request):

   return render(request, 'displayDepartureFlights.html')

def displayReturningFlights(request):

   return render(request, 'displayReturningFlights.html')

def displaySelectedDepartureFlight(request):

   return render(request, 'displaySelectedDepartingFlight.html')

def displaySelectedReturningFlight(request):

   return render(request, 'displaySelectedReturningFlight.html')

def displayItenary(request):

   return render(request, 'displayItenary.html')

def displayPassengerPage(request):

   return render(request, 'displayPassengerPage.html')

def reviewDetails(request):

   return render(request, 'reviewDetails.html')

def bookingConfirmation(request):

   return render(request, 'bookingConfirmation.html')


def submitexploreform(request):
  try:
    
    if request.method=="POST":

      tripD = str(request.POST.get('trip'))
      fromD = str(request.POST.get('from')) 
      toD = str(request.POST.get('to')) 
      departD = str(request.POST.get('startdate')) 
      returnD = str(request.POST.get('enddate')) 
      passangerD = str(request.POST.get('passanger'))

      request.session['returnDate']=returnD
      request.session['passanger']=passangerD

      
      data = {

            'tripD':tripD,
            'fromD':fromD,
            'toD':toD,
            'departD':departD,
            'returnD': returnD

      }

      
      FINALDATA = data
      print(data)
      
      if returnD == "":

       url = "/api/departureFlights/?trip={}&from={}&to={}&departure={}".format(tripD,fromD,toD,departD)
       return redirect(url)   
       
      else:

       url = "/api/departureFlights/?trip={}&from={}&to={}&departure={}&return={}".format(tripD,fromD,toD,departD,returnD)
       
       return redirect(url)
      
    return tripD
  
  except:
   pass


  
# check if its been used or not
def submitdepartureform(request):
      

      if request.method=="GET":
       

       selectedFlightId = request.GET.get("flight_id")
       print("Slected flight id id = {}".format(selectedFlightId))

       url = "/api/selectedDepartureFlight/?flightId={}".format(selectedFlightId)

       request.session['dFlightId'] = selectedFlightId


       return redirect(url)
 



      
def submitreturnform(request):
  
  try:
    if request.method=="POST":

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

# Check if its beenm used or not
def submitreturnselectedform(request):
      
      
      selectedReturnFlightId = request.GET.get("flight_id")
      print(selectedReturnFlightId)


      url = "/api/selectedReturningFlight/?flightId={}".format(selectedReturnFlightId)

      request.session['rFlightId'] = selectedReturnFlightId

      return redirect(url)


def submititenaryform(request):
  try:
    
    if request.method=="POST":

      #departingFlight = request.POST.get('departingFlightId')
      #returningFlight = request.POST.get('returningFlightId')
      returningFlight = request.session['rFlightId']
      departingFlight = request.session['dFlightId']
      passanger = request.session['passanger']
      

      data = {

            'departingFlight':departingFlight,
            'returningFlight':returningFlight

      }


      url = "/api/itenary/?trip={}&departingFlight={}&returningFlight={}&passanger={}".format("ROUNDTRIP",departingFlight,returningFlight,passanger)

      return redirect(url)
  except:
   pass
  
def submititenaryPage(request):
  try:
    
    if request.method=="POST":
       
      tripData = request.POST.get("tripStr")
      tripId = request.POST.get("trip_id")
      print(tripData)
      print(tripId)

      request.session['tripInfo'] = tripData
      request.session['trip_id'] = tripId


      passanger = request.session['passanger']
      print(passanger)
      

      data = {
            'passanger':passanger,
      }

      url = "/api/passangerPage/?passanger={}".format(passanger)

      return redirect(url)
      
  except:
   pass
  
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

  
  
def submitpassangerPage(request):

  if request.method=="POST":

   fName = str(request.POST.get('firstName'))
   lName = str(request.POST.get('lastName')) 
   dob = str(request.POST.get('dob')) 


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
   passangerId= result_json["id"]

   print(passangerId)


   request.session['passanger_id'] = passangerId
 



   #Need a logic to fetch passangerId


    
   tripD = request.session['tripInfo']

   pData = {

            "fName":fName,
            "lName":lName,
            "dob": dob

      }

   url = "/api/reviewDetails/?passanger={}&trip={}".format(pData, tripD)

   return redirect(url)
  
@csrf_exempt
def submitreviewform(request):
  

  try:
    
    if request.method=="POST":

      cardName = str(request.POST.get('cname'))
      cardNumber = str(request.POST.get('ccnum')) 
      expmonth = str(request.POST.get('expmonth')) 
      expyear = str(request.POST.get('expyear')) 
      cvv = str(request.POST.get('cvv')) 

      
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
    cardId= result_json["id"]

    request.session['card_id'] = cardId

   #Making call to POST Booking
    
    #Fetch Trip Id
    trip_Id = request.session['trip_id']
    print("TRIi={}".format(trip_Id)) 
  
    #Fetch Passanger Id
    passanger_Id = request.session['passanger_id']

    #Fetch Card Id
    card_Id = request.session['card_id']
    
    bookingRefernceNumber= ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    tripId=trip_Id
    passangerId= passanger_Id
    cardId = card_Id
    isMember= False
    contactEmail= "gurkirat2773@gmail.com"

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
    BookingId= result_json["bookingReferenceNumber"]



    url = "/api/bookingConfirmation/?bookingReferenceNumber={}".format(bookingRefernceNumber)



    return redirect(url)


  except:
    pass
  