# Name: Jagroop Singh 
# Student ID: 303105803
# Instructor: Dr. Syed Badruddoja

# COre dataset which will store all of the inpuuted values
dataset = []

# Populating dataset with user inputted values
for i in range(20):
    
    # print("Please enter a number: ")
    num = input("Please enter a number: ")
    
    # Converting our user input to an integer
    intNum = int(num)
    
    # Storing the user inputted integer in our list
    dataset.append(intNum)

# returns sum of all values in main dataset
def sumOfList():
    # Base variable which will store the final sum
    totalSum = 0
    
    # Iterating through our list
    for i in range(len(dataset)):
        
        # Adding each value in list to totalSum 
        totalSum += dataset[i]
    
    # Printing the summation of all values in the list
    print("Total Sum of Numbers in List: " + str(totalSum))
    
# returns all prime values in the dataset
def checkPrime():
    # Formatting the console output correctly
    print()
    print("Prime Numbers in the List: ", end="")
    
    # List which will be used to store the prime numbers from the main dataset
    primeDataset = []
    for i in range(len(dataset)):
        # Edge case disregarding 1 as a prime number
        if (dataset[i] <= 1):
            continue
       # Using a boolean value to only add prime numbers to our prime dataset
        # Initial value for this boolean will be set to True
        intPrime = True
        
        # checking to see if any value between 2 and dataset[i] - 1, leads to a value
        # of 0 when using the modulo operatoir
        for j in range(2, dataset[i], 1):
            
            # if any value returns 0 when using the modulo operator
            # update boolean value to false, meaning it will not be added to prime dataset
            if dataset[i] % j == 0:
                intPrime = False
                break
        # if value is prime, then add it to the prime dataset
        if (intPrime == True):
            primeDataset.append(dataset[i])
     
     # outputting all of the values from the prime dataset           
    for i in range(len(primeDataset)):
        print(primeDataset[i], end=", ")
                
# returns all numbers of the Fibonacci Sequence to a given user inputted value
def fibonacciSequence():
    
    fibonacciTerms = int(input("Please enter total number of terms for Fibonacci series: "))

    firstPtr = 0
    secondPtr = 1
    
    print("Fibonacci Series of " + str(fibonacciTerms) + " terms: ", end="")
    
    # edge case in case user only wants the first output of the sequence
    if (fibonacciTerms == 1):
        print(firstPtr)
    
    else:
        # Outputting 0 to console
        print(firstPtr, end=", ")
    
        # Outputting 1 to console
        print(secondPtr, end=", ")
    
        for i in range(2, fibonacciTerms):
        
            # Setting summation = to the sum of firstPtr and secondPtr
            # Fibonacci sequence is based on the principle of adding the 
            # two previous numbers to get a new number, so on and so forth
            summation = firstPtr + secondPtr
        
            # Updating firstPtr to have an updated value,moving firstPtr up by 1 index
            firstPtr = secondPtr
        
            # Updating secondPtr to have an updated value, moving secondPtr up by 1 index
            secondPtr = summation
        
            # Printing the curret summation value
            print(summation, end=", ")


# Main function calls
sumOfList()
fibonacciSequence()
checkPrime()


