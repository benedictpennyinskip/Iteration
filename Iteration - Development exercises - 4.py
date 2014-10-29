#Ben Penny-Inskip
#29/10/2014
#Iteration - Development exercises - 4

number = int(input("Please enter a number"))
largest = number
while number != -1:
    number = int(input("Please enter a number"))
    if number > largest:
        largest = number
print("The largest number is {0}".format(largest))