import math
while(True):

    let_play = input("Are you want to play the game :".title()).lower()
    while (let_play != "yes" and let_play != "no"):
        let_play = input("please answar must be yes/no :".title()).lower()
    else:
        if let_play == 'no':
            print("You can play it Next Time . Good bye ! TaTA .")
            exit()
        else:
            print("( WELLCOME TO GAME LOBBY )".center(80, "-"))
            print("The game is about guassing a (program chosed) number between your range :".title())
            print("".center(80, "-"))
            #                     Entering range value
            range_lower = input("Enter the lower value of range :".title())
            range_upper = input("Enter the upper value of range :".title())
            #                     checking for value
            while (not range_lower.isdigit() or not range_upper.isdigit()):
                print("Both value must be integer :")
                range_lower = input("Enter the lower value of range :".title())
                range_upper = input("Enter the upper value of range :".title())
            else:
                range_lower = int(range_lower)
                range_upper = int(range_upper)
                randam = int(((range_upper + range_lower) * 0.3) + ((range_upper - range_lower) / 2))
                min_chance = round(math.log((range_upper - range_lower), 2))
                trying = 0
                print(f"( You have totall {min_chance - trying} chance )".center(80, "_"))
        user_choise = float(input("Now Guess a number between your range :".title()))
        while (user_choise < range_lower or user_choise > range_upper):
            user_choise = float(
                input(f"Guess number must be between your range {range_lower} To {range_upper}:".title()))
        else:
            while (user_choise != randam):
                if trying + 1 != min_chance:
                    trying = trying + 1
                    if user_choise < randam:
                        print(f"( NOTE )-->    Your chosen {int(user_choise)} is less then Guessed  \n")
                    else:
                        print(f"( Your chosen {int(user_choise)} is Greater then Guessed )".center(80, '#'), "\n")
                    print(f"only {min_chance - trying} tries left :".center(80, "-"))
                    user_choise = float(input("Wrong guessed! \n try again :"))
                else:
                    print("Good luck Next time :")
                    break
            else:
                print(f"\nCongratulation you guessed correct in {trying + 1} Try :".title())
                print("lets play again".title().center(80, '-'))