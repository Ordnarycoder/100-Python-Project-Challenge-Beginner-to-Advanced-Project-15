import random

def number_guess():
    user_num = int(input("Please enter a number between 1 and 10:\n")) 
    computer_num = random.randint(1, 10)
    print(f"Computer picked: {computer_num}")
    
    if user_num == computer_num:
        print(f"You guessed right! Computer Number: {computer_num}\nPlayer Number: {user_num}")
    else:
        print(f"You guessed wrong! Computer Number: {computer_num}\nPlayer Number: {user_num}")

number_guess()
