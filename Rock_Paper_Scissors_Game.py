from colorama import Fore

try:
    def game_logic(computer_choice, user_choice, user_score, computer_score):
        if computer_choice == 'rock' and user_choice == 'p':
            print(player_name + " Wins")
            print("Enter 1 to continue and 0 to leave the game")
            user_score += 1
            i1 = input()
            return i1, user_score, computer_score
        elif computer_choice == 'rock' and user_choice == 's':
            print("Computer Wins")
            print("Enter 1 to continue and 0 to leave the game")
            computer_score += 1
            i1 = input()
            return i1, user_score, computer_score
        elif computer_choice == 'paper' and user_choice == 'r':
            print("Computer Wins")
            print("Enter 1 to continue and 0 to leave the game")
            computer_score += 1
            i1 = input()
            return i1, user_score, computer_score
        elif computer_choice == 'paper' and user_choice == 's':
            print(player_name + " Wins")
            print("Enter 1 to continue and 0 to leave the game")
            user_score += 1
            i1 = input()
            return i1, user_score, computer_score
        elif computer_choice == 'scissors' and user_choice == 'r':
            print(player_name + " Wins")
            print("Enter 1 to continue and 0 to leave the game")
            user_score += 1
            i1 = input()
            return i1, user_score, computer_score
        elif computer_choice == 'scissors' and user_choice == 'p':
            print("Computer Wins")
            print("Enter 1 to continue and 0 to leave the game")
            computer_score += 1
            i1 = input()
            return i1, user_score, computer_score
        elif (computer_choice == 'rock' and user_choice == 'r') or (computer_choice == 'paper' and user_choice == 'p') or (computer_choice == 'scissors' and user_choice == 's'):
            print("Draw")
            print("Enter 1 to continue and 0 to leave the game")
            user_score += 1
            computer_score += 1
            i1 = input()
            return i1, user_score, computer_score


    def user_input_checker():
        user_choice = input("Enter your choice:")
        if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
            return user_choice
        else:
            print("Wrong Input!!")
            return 0


    import random

    choices = ['rock', 'paper', 'scissors']
    print(Fore.LIGHTCYAN_EX + "Welcome to the game!")
    print(Fore.CYAN + "Enter:\nr for rock\np for paper\ns for scissors")
    player_name = input(Fore.YELLOW + "Enter your name:")
    i = '1'
    user_score_total = 0
    computer_score_total = 0
    while i == '1':
        user_input = user_input_checker()
        while user_input == 0:
            user_input = user_input_checker()
        computer_choice = random.choice(choices)
        print("Computer chooses:" + computer_choice)
        i, computer_score_total, user_score_total = game_logic(computer_choice, user_input, user_score_total, computer_score_total)
        if i == '0':
            print(Fore.MAGENTA + "Scores for this match are as follows:")
            print(Fore.BLUE + player_name + "'s score: ", user_score_total)
            print(Fore.BLUE + "Computer's score: ", computer_score_total)
            print(Fore.GREEN + "Thank you for playing the game.\nHave a nice day!!")
        elif i != '0' and i != '1':
            print(Fore.RED + "Invalid Input!!")
            i = int(input("Please enter 1 to continue or 0 to leave the game:"))


except Exception as e:
    print(Fore.RED + "Error Occurred!!\nPlease restart the game.")
