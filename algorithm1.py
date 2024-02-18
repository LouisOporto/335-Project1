from random import sample

# Algorithm 1

def swap_partner(myList):
    """Given a list of unique numbers, will return swapped partners
    with 1/2n swaps."""
    number_swapped = 0
    
    # Iterate through every other element of the loop (ie. [0],[2],[4])
    # The adjacent index will be where the partner will be swapped
    for element in range(0, len(myList), 2):
        # Check if the partner we are targeting for is the odd or even partner
        if myList[element] % 2 == 0:
            partner_number = myList[element] + 1  # Target is odd partner
        else:
            partner_number = myList[element] - 1  # Target is even partner
        
        # Loop through the rest of unswapped list for the partner and place it beside
        for number in range(element + 1, len(myList)):
            if myList[number] == partner_number:
                # In-place swapping values
                myList[number] = myList[element + 1] 
                myList[element + 1] = partner_number
                number_swapped += 1  # Successful swap adds to the counter
                break  # Next pair to check for
    return number_swapped 


randomList = sample(range(0, 30), 30)  # Using sample to simulate a random list of partners of size 30
print(f"Unswapped: {randomList}")
print(swap_partner(randomList))
print(f"Swapped: {randomList}")
# It takes 1/2n swaps to complete swapping.