#Class Exercises - Iteration Statements - Strech Task 1
#Ben penny Inskip
#30/10/2014

number = int(input("Please enter a number:"))

for counter in range(number+1):
    square = counter**2
    print("{0:>3}^2 {1:<3}".format (counter, square))