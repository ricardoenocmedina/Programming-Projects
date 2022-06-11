ZERO = "0"
ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"
ERRORMESSAGE = "ERROR: Illegal value entered."
ILLEGALCOMMAND = "ERROR: Illegal command. Try again."


def firstNFibNumbers(n):
    """ Returns a list of the first n Fibonnaci numbers.  If 
        n < 0, returns an error message. If n = 0, returns and empy list """

    if n < 0:
        return ERRORMESSAGE
    
    elif n == 0:
        return []

    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        return [ 0 ]
    elif n == 2:
        return [ 0, 1 ]

    # Here we know that n is at least 2.
    else:

        # Initialize fib1 and fib2 with the first 
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1

        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [ 0, 1 ]

        # Use the previous two values to generate 
        # and record the next value.
        for counter in range( 2, n ):

            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2

            # Add the newest value to the list we're
            # creating.
            fibs.append( fib2 )

        return fibs

def ithFibNumber():
    """ Returns the ith Fibonnaci number. If n < 0, return an error message"""
    
    n = int(input("You've asked for the ith Fibonnaci number. What is it? "))

    # Edge case if n is negative
    if n < 0 :
        print(ERRORMESSAGE)
        return
    
    elif n == 0:
        print(0)
        return

    elif n == 1:
        print(1)
        return
    
    elif n == 2:
        print(1)
        return
    
    else:
        # n + 1 in order to avoid range error in this part of the code
        n = n + 1
        fib1, fib2 = 0, 1
        fibs = [0, 1]
        
    for counter in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        
        fibs.append(fib2)
    # pop function to find the ith term
    print(fibs.pop(n-1))
    return

def fibListLessThanN():
    """Returns a list with fibonacci numbers that are less than or equal to N"""
    
    n = int(input("You've asked for the Fibonacci numbers less than or equal to N. What is N?: "))

    # prints an empty bracket for 0 or less
    if n <= 0:
        print("[]")
        return

    # Handle the cases of n = 1 specially.
    elif n == 1:
        print("[0]")
        return

    fib1, fib2 = 0, 1
        
    fibs = [ 0, 1 ]

    # Here we know that n is at least 2.
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        
        if fib2 > n:
            break
        
        else:
            fibs.append(fib2)
            continue
        
    # returns this list instead of the ith term, like in the last method 
    print(fibs)
    return

def howManyFibNums():
    """Returns the number of fibonacci numbers that are less than or equal to N."""
       
    
    n = int(input("You've asked for how many Fibonacci numbers are less than or equal to N. What is N? "))

    # for negative numbers, it will return 0
    if n < 0:
        print(0)
        return

    # Handle the cases of n == 0 specially.
    elif n == 0:
        print(1)
        return

    fib1, fib2 = 0, 1
        
    fibs = [ 0, 1 ]

    # follows the same code as the other methods
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        
        if fib2 > n:
            break
        
        else:
            fibs.append(fib2)
            continue
        
    # prints the length of the list, instead of the list itself
    print(len(fibs))
    return

def listOfLargestFibNums():
    '''Returns a list of the largest Fibonacci numbers that add up to N.
       If n < 0, return error message.'''
    
    n = int(input("You've asked for Fibonacci numbers that sum to N. What is N? "))

    # Defining constants and an empty list
    x = -1
    sum1 = 0
    newList = []
    
    fib1, fib2 = 0, 1    
    fibs = [ 0, 1 ]
    # the following while loop is borrowed from the past methods
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        
        if fib2 > n:
            break
        else:
            fibs.append(fib2)
            continue
    # if n is negative, print error message
    
    if n < 0:
        print(ERRORMESSAGE)
        return
    
    # this while loop continously adds and replace to the newList
    while True:
        # will break the loop if the sum is greater than the N being asked
        if sum1 >= n:
            break

        # append if the sum and the ith term is less than the desired N
        elif (sum1 + fibs[x]) <= n:
            newList.append(fibs[x])
            
        # "resets" the sum count
        sum1 = 0
        x = x - 1
        
        # adds to the sum in order to determine when to stop since it is a countinous while loop
        for z in range(len(newList)):
            sum1 = sum1 + newList[z]
            

    print(newList)
    return
            
        
            
            
            

def main():
    '''The main function, where all other functions are called from and displayed'''
    
    print("\nWelcome to the Fibonnacci Number Laboratory!\n")
    print("The following commands are available:\n  0: Exit.\n  1: List the first N Fibonnaci numbers.\n  2: Display the ith Fibonnaci number (0-based).\n  3: List the Fibonnaci numbers less or equal to N.\n  4: How many Fibonnaci numbers are less or equal to N?\n  5: Find a list of the largest Fibonnaci numbers that add up to N.\n  6: Display this help message.")

    while True:
        userInput = input("\nPlease enter a command (0, 1, 2, 3, 4, 5 or 6): ")
        
        if userInput == ZERO:
            print("\nThanks for using the Fibonnaci Laboratory! Goodbye.")
            break
        
        elif userInput == ONE:
            userInput2 = int(input("You've asked for the first N Fibonnaci numbers. What is N? "))
            print(firstNFibNumbers(userInput2))
            
        elif userInput == TWO:
            ithFibNumber()
            
        elif userInput == THREE:
            fibListLessThanN()

        elif userInput == FOUR:
            howManyFibNums()
            
        elif userInput == FIVE:
            listOfLargestFibNums()

        elif userInput == SIX:
            print("The following commands are available\n  0: Exit.\n  1: List the first N Fibonnaci numbers.\n  2: Display the ith Fibonnaci number (0-based).\n  3: List the Fibonnaci numbers less or equal to N.\n  4: How many Fibonnaci numbers are less or equal to N?\n  5: Find a list of the largest Fibonnaci numbers that add up to N.\n  6: Display this help message.")

        else:
            print(ILLEGALCOMMAND)
            print("\nThe following commands are available:\n  0: Exit.\n  1: List the first N Fibonnaci numbers.\n  2: Display the ith Fibonnaci number (0-based).\n  3: List the Fibonnaci numbers less or equal to N.\n  4: How many Fibonnaci numbers are less or equal to N?\n  5: Find a list of the largest Fibonnaci numbers that add up to N.\n  6: Display this help message.")

main()
