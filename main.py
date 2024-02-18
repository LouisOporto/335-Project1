from random import sample

# Algorithm 1

def swap_partner(myList):
    number_swapped = 0
    for element in range(0, len(myList), 2):
        if myList[element] % 2 == 0:
            partner_number = myList[element] + 1
        else:
            partner_number = myList[element] - 1
        for number in range(element + 1, len(myList)):
            if myList[number] == partner_number:
                myList[number] = myList[element + 1]
                myList[element + 1] = partner_number
                number_swapped += 1
                break
    return number_swapped


randomList = sample(range(0, 30), 30)
print(f"Unswapped: {randomList}")
print(swap_partner(randomList))
print(f"Swapped: {randomList}")
# It takes 1/2n swaps to complete swapping.

# Algorithm 2

def starting_city(cities, gas):
    city_length = len(cities)
    start_city = 0
    for city in range(0, city_length):
        counter, city_number = city_length, city  # Counter to loop through all cities, starting city
        miles_left =  0  # Miles left with gas left
        city_pass = True  #  Will be False if trip is not traversable.

        while counter != 0:  # Simulate a trip from starting city in a loop. Breaks
            if city_number >= city_length: city_number = 0
            
            # Calculation to check if the amount of gas converted to miles avaiable with gallons.
            miles_left += gas[city_number] * 10
            miles_left = miles_left - cities[city_number]

            if miles_left < 0: 
                city_pass = False
                break

            city_number += 1
            counter -= 1

        if city_pass:
            start_city = city

    return start_city


cities = [25,15,10,15,5]
gas = [2,1,0,3,1]
# Should return 3 in this example
print(starting_city(cities,gas))