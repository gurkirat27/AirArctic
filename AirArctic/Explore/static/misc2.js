
   
async function makeTrip(selectedDepartingFlight, selectedReturningFlight) { 

        
            
    const rawResponse = await fetch(`http://127.0.0.1:8000/api/trips/?trip=${trip}`, {
      method: 'POST',
      body: JSON.stringify({
        "departingFlight_id": selectedDepartingFlight,
        "returningFlight_id": selectedReturningFlight,

      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
     },
  });
  const content = await rawResponse.json();

  console.log(content);
  return content;
  

    }


   
   
async function getFlights(from, to, departure) {
      
        let head= new Headers();
        

        headers.append('Content-Type', 'application/json');
        headers.append('Accept', 'application/json');
        headers.append('Origin','http://localhost:8000');

        let flights =await fetch(`http://127.0.0.1:8000/api/flights/?departureAirport=${from}&destinationAirport=${to}&departureDate=${departure}`,{headers:head});

        flights = await flights.json()
        console.warn(flights)
        return flights


        console.log("Orignal func")

}

async function getFlightById(flightId) {




  let flight =await  fetch(`http://127.0.0.1:8000/api/flight/${flightId}`);

  flight = await flight.json()
  console.warn(flight)
  return flight


  console.log("GetFlight by If func")

}


function storesTripData(from, to){

  console.log(from)
  console.log(to)

}




    async function getReturningFlights(from, to) {



        let flights =await  fetch(`http://127.0.0.1:8000/api/flights/?departureAirport=${to}&destinationAirport=${from}`);
    
        flights = await flights.json()
        console.warn(flights)
        return flights
        
    }

  



    function storeDepartingFlightId(selectedDepartingFlightId){
      console.log(selectedDepartingFlightId);
      return selectedDepartingFlightId;
      
    }

    function takeToReturningFlightPage(){
      return window.location.href = "{% url 'displayDepartureFlights' %}"
    
    }

    

   

