import random
import math

problems = int(input("How many problems do you want?\n"))

def main(problems):
    random.seed()
    count = 0
    correct = 0

    while count < problems:
        a = random.randint(0,12)
        b = random.randint(0,12)
        guess = int(input("What is " + str(a) + " X " +str(b) + "? "))
        answer = int(a * b)
        count += 1

        if guess == answer:
            correct += 1
            print("\nCorrect!\n")
        else:
            print("\nSorry, the answer is", answer, ".\n")

    if problems > 1:
        result = correct/problems * 100
    print("\nYou got ", "%.1f"%result, "% of the problems correct.")

main(problems)

    
