# Algorithm 2

def starting_city(cities, gas):
    """Given a list of cities and gas, will simulate each trip from each city as starting and returns
    city that completes a loop."""
    city_length = len(cities)

    # Each city will be tested as starting city
    for city in range(0, city_length):
        counter, city_number = city_length, city  # Counter to loop through all cities, starting city
        miles_left =  0  # Miles left with gas left
        city_pass = True  #  Will be False if trip is not traversable.

        # Simulate the trip
        while counter != 0:  # Simulate a trip from starting city in a loop. Breaks
            if city_number >= city_length: city_number = 0

            # Calculation to check if the amount of gas converted to miles avaiable with gallons.
            miles_left += gas[city_number] * 10
            miles_left = miles_left - cities[city_number]

            # If miles_left is negative then there isn't enough gas
            if miles_left < 0:
                city_pass = False
                break

            # Iterate counters to next city and reloop city track.
            city_number += 1
            counter -= 1

        # If city_pass is True after simulation, return the city
        if city_pass:
            return city

    return None  # Only returns if none of the cities pass

# Document Example - (Should return index 4)
cities = [5,25,15,10,15]
gas = [1,2,1,0,3]

print(starting_city(cities,gas))
