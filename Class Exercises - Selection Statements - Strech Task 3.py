#Class Exercises - Selection Statements - Strech Task 3
#Ben penny Inskip
#01/11/2014

binaryNumber = str(input("Please enter an 8bit binary number"))
add = 128
denaryNumber = 0

for counter in range(8):
    print(counter)
    number = binaryNumber[counter]
    if number == "1":
        denaryNumber = denaryNumber + add
    add = add / 2
print(denaryNumber)