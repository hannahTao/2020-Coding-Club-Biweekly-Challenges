def square_difference(n):
    sumOfSquares = 0
    sumOfIntegers = 0
    for i in range (n+1):       # find sum of squares of integers
        sumOfSquares += n**2
    for j in range (n+1):       # find square of sum of integers
        sumOfIntegers += n
    return sumOfIntegers**2 - sumOfSquares  # calculate difference
    
square_difference(10)          # example should equal 2640
square_difference(100)         # answer 
