# Rock paper Scissors game using random module :-

"""
Rock vs paper --> paper wins
Rock vs Scissors --> Rock wins
Paper vs Scissors --> scissor wins

- Total 5 rounds
- store rock , paper and scissor in a list computer generates a random from that list and then it is compared with the
  user input on basis of this result is generated at each round and the player with most count wins .

"""
import random

li = ['r', 'p', 's']

while True:
    print("\n `````````````````` ROCK PAPER SCISSORS `````````````````````` \n")
    print(
        "\nRULES :-\nThere will be 5 rounds \nWinning Rules are -\nRock vs paper --> paper wins\nRock vs Scissors --> Rock wins\nPaper vs Scissors --> scissor wins \n")
    print("press :-\nr for ROCK\np for paper\ns for scissors")

    cc = 0
    ic = 0
    for a in range(5):
        print("\n----------------------------\nRound ", a + 1, "\n----------------------------")
        i = input("\nEnter your choice : ")
        i.lower()
        c = random.choice(li)

        if i == c:
            print("\nYou chose : ", i, "    |    Computer chose : ", c)
            print("\nDraw !!")

        elif i == 'p' and c == 'r' or i == 's' and c == 'p' or i == 'r' and c == 's':
            print("\nYou chose : ", i, "    |    Computer chose : ", c)
            print("\nyeh!!! you got a point")
            ic = ic + 1

        elif i == 'r' and c == 'p' or i == 'p' and c == 's' or i == 's' and c == 'r':
            print("\nYou chose : ", i, "    |    Computer chose : ", c)
            print("\nComputer got a point")
            cc = cc + 1

        else:
            print("\nTry again !!!!")
            break

    if ic == cc:
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   Result Time ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        print("\nGame is Draw !!!!")
    elif ic > cc:
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   Result Time ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        print("\nCongrats !!!!! You won !!!!!!!")
    elif cc < ic:
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   Result Time ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        print("\nComputer won !! Better luck next time ")
    else:
        break
    ch = int(input("\ndo you want to play again ? "
                   "\n1 = Yes"
                   "\n2 = No "
                   "\nYour choice : "))
    if ch == 1:
        continue
    else:
        break
