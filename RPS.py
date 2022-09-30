#Rock Paper Scissor
import random

user = 0
comp = 0

options = ["rock", "paper", "scissor"] #a list
# options at 0 will give rock, at 1 it will give paper and so on

while True:
    user_input = input("ROCK/PAPER/SCISSOR? or Q to Quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue


    random_no = random.randint(0,2)
    # rock: 0, paper: 1, scissor:2
    comp_pick = options[random_no]

    print("Computer picked ", comp_pick)

    if user_input == "rock" and comp_pick == "scissor":
        print("You WON!")
        user += 1
        continue

    elif user_input == "paper" and comp_pick == "rock":
        print("You WON!")
        user += 1
        continue

    elif user_input == "scissor" and comp_pick == "paper":
        print("You WON!")
        user += 1
        continue

    elif user_input == comp_pick:
        print("TIE!")
        comp += 1
        user += 1
        continue
    
    else:
        print("Comp WON! You lost..")
        comp += 1

print("You won ", user, " times!")
print("Computer won", comp, " times!")

if user == comp:
    print("You and computer had a tie!")

elif user > comp:
    print("You are the ultimate WINNER! Congratulations!")

else:
    print("Computer is the Winner of the match")

print("Goodbye!")