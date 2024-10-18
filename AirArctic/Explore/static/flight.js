async function getFlights(from, to) {



    let flights =await  fetch(`http://127.0.0.1:8000/api/flights/?departureAirport=${from}&destinationAirport=${to}`);

    flights = await flights.json()
    console.warn(flights)
    document.getElementById('flightData').innerHTML=flights.map((flight) => 
        `<tr>
            <td>${flight.id}</td>
            <td>${flight.flightNumber}</td>
            <td>${flight.departureAirport.iataCode}</td>
            <td>${flight.destinationAirport.iataCode}</td>
            <td>${flight.departureDate}</td>
            <td>${flight.departureTime}</td>
            <td>${flight.arrivalDate}</td>
            <td>${flight.arrivalTime}</td>
            <td><input type="button"  value="Select Flight" onClick="getDepartingFlightId()"> </td>
        </tr>`
    
    ).join("");
     
    var departingFlightId = flight.id;

}