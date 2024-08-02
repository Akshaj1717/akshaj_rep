import random
import math
#taking inputs
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

#generating random number between lower and upper
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")

#initialize number of guesses
count = 0
flag = False

#calculation of minimum number
while count < total_chances:
    count += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congratulations you did it in ", count, " try")
        flag = True
        break
    elif x > guess:
        print("Try again! Guess was too small")
    elif x < guess:
        print("Try again! Guess was too high")
if not flag:
    print("\nthe number is %d" % x)
    print("\tBetter luck next time")