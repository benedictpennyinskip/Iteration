#Class Exercises - Selection Statements - Strech Task 4
#Ben penny Inskip
#02/11/2014

sentence = (input("Please enter a sentence:"))
wordCount = 0

for counter in range(len(sentence)):
    chacacter = sentence[counter]
    if chacacter == " " or chacacter == ".":
        wordCount = wordCount + 1


print("This sentence has {0} words".format(wordCount))
