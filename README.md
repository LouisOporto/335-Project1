# Project 1

>  **Students**
> - Louis Oporto

\* This will be the README.md to explain how my algorithm works for both algorithm 1 and 2 \*

## Algorithm 1
### Pseudocode
Will use an in-place selection sort. Swapping until elements neighbor their partners.
The for loops

    function swap_partners(N list of 2n with comparable objects):

        let number_swapped = 0 (counter for swaps)

        for every even element in length of N do
            if (N[element] % 2 == 0) (partner is N[element] + 1) do
                partner_number = N[element] + 1
            else do
                partner_number = N[element] - 1

            for each number after element in N do
                if N[element + 1] == partner_number: (partner is already paired)
                    break

                if number == partner_number do
                    N[element + 1] = number (In-place swapping)
                    number_swapped += 1

    return number_swapped

###  Complexity and Efficiency Class
/*TODO*/
loop that iterates 1/2n
    (n-1)+(n-3)+...+1=summation comparsion

### How it Works
To run this algorithm type `py algorithm1.py`
Will create a pseudorandom sample of 30 unique numbers in a list.

Given a list that is assumed even and unique with a size n < 30, it will iterate through every other element to pair up neighbor numbers. We iterate by twos because the pair number will be in the next index if swapping is done correctly. We check if the current number is even or odd to know if the partner number is +1(if even) or -1(if odd). We then iterate, in the unswapped portion of the list to find this partner number and swap in-place. If the number is already paired, then we will not swap. Swapping is complete once we get to the last pair to swap. It will return the number of times the algorithm had swapped.

### Files Included
algorithm1.py


## Algorithm 2
### Pseudocode
Run through each city as the starting city and return the index if completes an entire cycle.

    function starting_city(cities list of city distances of size n, gas list of gas within each city of size n):
    let city_length = length of cities

    for every element in cities do
        let counter = city_length (Counter to zero)
        let city_number = element (current city we are starting)
        let miles_left = 0 (Miles counter)
        city_pass = True (False if starting city fails)

        while counter is not 0 do
            if city_number >= city_length do
                city_number = 0 (Loops back to cities[0])

            miles_left += gas[city_number] * 10 (Add gas from current city converted to miles)
            miles_left = miles_left - cities[city_number]  (Subtract the distance to next city)

            if miles_left < 0 do
                city_pass = False
                break (Current routine will not loop so break and try next)

            city_number++
            counter--

        if city_pass do
            return city

    return None (No city works)

###  Complexity and Efficiency Class
/*TODO*/
Loops for n cities
    Looping through 5 cities and stopping early if best city is found

### How it Works
To run this algorithm type `py algorithm2.py`
Will use the example provided in the Project 1 document. (Should return 4)

Given a list of city distance from the next neighboring city and a list of available gas within that indexed city, it will return the best city to start your round trip.
The algorithm will iterate through each city simulating it as the starting point for each trip. We then iterate through each city in a clockwise order until we return to the starting city. If at any time on the simulation that our gas is below the required traveling distance to the next city, we end it and continue to the next simulation. If the city succeeds at completing a loop then return that city index immediately.

### Files Included
algorithm2.py
