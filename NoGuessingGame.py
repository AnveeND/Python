# Number guessing game using random module
"""
Computer will generate one random number
user will give one number as input
then compare both these numbers
"""

import random as r

print("\n~~~~~~~~~~~~~~~~~~~~~~ Number Guessing Game ~~~~~~~~~~~~~~~~~~~~~~~\n")
print("- Game will have total five rounds to guess a number \n- Correct guess will end the game \n- Guess the number only between 1 to 100 ")
n = r.randint(1, 100)
for x in range(5):

    i = int(input("\nGuess one number : "))
    if n == i:
        print("\nBRAVO!! Correct Guess\nYou Win !!!!!!!!!!! ")
        break
    else:
        if i < n and x != 4:
            print("\n*HINT - Number is greater  ")
            print("\nTry again !! (chances remaining = ", 4-x, ")")
        elif i > n and x != 4:
            print("\n*HINT - Number is smaller ")
            print("\nTry again !! (chances remaining = ", 4-x, ")")
        else:
            print("\nOpps!! Game Over")
            print("\nThe number was : ", n)


