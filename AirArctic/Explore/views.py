from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def explore(request):

   return render(request, 'exploreTrip.html')

def displayDepartureFlights(request):

   return render(request, 'displayDepartureFlights.html')

def displayReturningFlights(request):

   return render(request, 'displayReturningFlights.html')

def displaySelectedDepartureFlight(request):

   departureFlightId = request.GET.get('id')

   request.session['dFlightId'] = departureFlightId

   return render(request, 'displaySelectedDepartingFlight.html')

def displaySelectedReturningFlight(request):

   return render(request, 'displaySelectedReturningFlight.html')

def displayItenary(request):

   return render(request, 'displayItenary.html')

def submitexploreform(request):
  try:
    if request.method=="POST":

      tripD = str(request.POST.get('trip'))
      fromD = str(request.POST.get('from')) 
      toD = str(request.POST.get('to')) 
      departD = str(request.POST.get('startdate')) 
      returnD = str(request.POST.get('enddate')) 

      request.session['returnDate']=returnD

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
      
    #return redirect(url)
      
      
    
      
    #return render(request, "displayReturningFlights.html", data)

  except:
   pass

  
  
def submitdepartureform(request):
      

      
      

      if request.method=="GET":
       
       dD = submitexploreform(request)
       print("DB IS"+ dD)

       selectedFlightId = request.GET.get("flight_id")
       print("Slected flight id id = {}".format(selectedFlightId))

       flightId = 1

       url = "/api/selectedDepartureFlight/?flightId={}".format(selectedFlightId)

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

      print("FROM D VALUE IS" + fromD)
      print(toD)

      #url = "/api/returningFlights/?trip={}&from={}&to={}".format("ROUNDTRIP",fromD,toD)
      url = "/api/returningFlights/?trip={}&from={}&to={}&return={}".format("ROUNDTRIP",fromD,toD,returnDate)

      return redirect(url)
  except:
   pass

def submitreturnselectedform(request):
      
      
      selectedReturnFlightId = request.GET.get("flight_id")
      print(selectedReturnFlightId)

      flightId = 1

      url = "/api/selectedReturningFlight/?flightId={}".format(selectedReturnFlightId)

      return redirect(url)

def submititenaryform(request):
  try:
    if request.method=="POST":

      #departingFlight = request.POST.get('departingFlightId')
      returningFlight = request.POST.get('returningFlightId')

      departingFlight = request.session['dFlightId']
      

      data = {

            'departingFlight':departingFlight,
            'returningFlight':returningFlight

      }


      url = "/api/itenary/?trip={}&departingFlight={}&returningFlight={}".format("ROUNDTRIP",departingFlight,returningFlight)

      return redirect(url)
  except:
   pass