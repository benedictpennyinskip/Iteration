#Class Exercises - Selection Statements - Strech Task 2
#Ben penny Inskip
#01/11/2014

remainder = int(input("Input a number from 0 - 255:"))
take = 128
result = " "
for counter in range(8):
    print(take)
    if remainder >= take:
        remainder = remainder - take
        result = result + "1"

    else:
        result = result + "0"
    take = take / 2
    print(result)
print(result)

