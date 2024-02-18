# Assignment 1

>  **Students**
> - Louis Oporto

\* This will be the README.md to explain how my algorithm works for both algorithm 1 and 2
\*

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
                if number == partner_number do
                    N[element + 1] = number
                    number_swapped += 1

    return number_swapped

###  Complexity and Efficiency Class
loop that iterates 1/2n
    (n-1)+(n-3)+...+1=summation comparsion

### How it Works

### Files Included

## Algorithm 2
### Pseudcode 
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
            miles_left = miles_left - cities[city_number]  (Substract distance to next city)

            if miles_left < 0 do
                city_pass = False
                break (Current routine will not loop so break and try next)
            
            city_number++
            counter--
        
        if city_pass do
            return city

    return None (No city works)

###  Complexity and Efficiency Class
Loops for n cities
    Looping through 5 cities and stopping early if best city is found

### How it Works

### Files Included