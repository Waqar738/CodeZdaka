import random
import math
from ai import call_gpt

develper = "ᵇʸ 𝕎𝕒𝕢𝕒𝕣 𝔸𝕗𝕣𝕚𝕕𝕚"
version = "𝕍𝕖𝕣𝕤𝕚𝕠𝕟 𝟚.𝟘"

def main():
    aval_feature = [
        [1, 2, 3],
        ["UNi Data", "Games", "Chat Bot"],
        [ustbdatakarel, gameskarel, chatbotkarel]
    ]
    tabulate(["ID", "Feature"], list(zip(aval_feature[0], aval_feature[1])))
    user_input = int(input("Select feature by id :".title()))
    while user_input not in aval_feature[0]:
        user_input = int(input("please select correct id :".title()))
    aval_feature[2][user_input - 1]()


# function that operate ustbdata
def ustbdatakarel():
    # chosing the data e.g Notes, past paper or ass....
    data = [
        [1, 2, 3],
        ["Notes", "Past Paper", "Assignment"],
        [UstbData.Notes, UstbData.PastPaper, UstbData.Assignment]
    ]
    tabulate(["ID", "Data"], list(zip(data[0], data[1])))
    user_input = int(input("Select DATA by id :".title()))
    while user_input not in data[0]:
        user_input = int(input("please select correct id :".title()))
    chosen_data = data[2][user_input-1]
    # chosing semester ....
    semester = [
        [1, 2, 3],
        ["1st semester", "2nd semester", "3rd semester"],
        [chosen_data.semester1st, chosen_data.semester1st, chosen_data.semester1st]
    ]
    tabulate(["ID", "Semester"], list(zip(semester[0], semester[1])))
    user_input = int(input("Select semester by id :".title()))
    while user_input not in data[0]:
        user_input = int(input("please select correct id :".title()))
    print("you can Download From Below links \U0001F447 :")
    semester[2][user_input-1]()



# function that operate all games
def gameskarel():
    aval_games = [
        [1],
        ["Number Guessing"],
        [Game.guessing]
    ]
    tabulate(["ID", "Games"], list(zip(aval_games[0], aval_games[1])))
    user_input = int(input("Select Game by id :".title()))
    while user_input not in aval_games[0]:
        user_input = int(input("please select correct id :".title()))
    aval_games[2][user_input - 1]()


# funtion that operate chat bot
def chatbotkarel():
    ChatBot()


# function that make table
def tabulate(headers, data):
    # Combine headers and data to calculate column widths
    cols = list(zip(*([headers] + data)))
    col_widths = [max(len(str(item)) for item in col) for col in cols]

    # Format a row with proper spacing and borders
    def format_row(row):
        return "| " + " | ".join(str(item).ljust(w) for item, w in zip(row, col_widths)) + " |"

    # Build borders
    def make_line(char):
        return "+" + "+".join(char * (w + 2) for w in col_widths) + "+"

    # Build each part of the table
    lines = []
    lines.append(make_line("-"))         # Top border
    lines.append(format_row(headers))   # Header row
    lines.append(make_line("="))        # Header separator
    for row in data:
        lines.append(format_row(row))   # Data row
        lines.append(make_line("-"))    # Line after each row

    # Join and print all lines with a single print()
    print("\n".join(lines))

class Game:     # All Games are managed here
    @staticmethod
    def guessing():
        while True:
            let_play = input("Are you want to play the game 🥰:".title()).lower()
            while let_play != "yes" and let_play != "no":
                let_play = input("please answar must be yes/no :".title()).lower()
            else:
                if let_play == 'no':
                    print("You can play it Next Time . Good bye ! TaTA 👋.")
                    print("Type *Quit* To Stop Program....")
                    exit()
                else:
                    print("( WELLCOME TO GAME LOBBY)".center(80, "-"))
                    print("The game is about guassing a (program chosed) number between your range :".title())
                    #                     Entering range value
                    range_lower = input("Enter the lower value of range :".title())
                    range_upper = input("Enter the upper value of range :".title())
                    #                     checking for value
                    while not range_lower.isdigit() or not range_upper.isdigit():
                        print("Both value must be integer :")
                        range_lower = input("Enter the lower value of range :".title())
                        range_upper = input("Enter the upper value of range :".title())
                    else:
                        range_lower = int(range_lower)
                        range_upper = int(range_upper)
                        randam = random.randint(range_lower, range_upper)
                        min_chance = round(math.log((range_upper - range_lower), 2))
                        trying = 0
                        print(f"( You have totall {min_chance - trying} chance )".center(80, "_"))
                user_choise = float(input("Now Guess a number between your range :".title()))
                while user_choise < range_lower or user_choise > range_upper:
                    user_choise = float(
                        input(f"Guess number must be between your range {range_lower} To {range_upper}:".title()))
                else:
                    while user_choise != randam:
                        if trying + 1 != min_chance:
                            trying = trying + 1
                            if user_choise < randam:
                                print(f"Your chosen {int(user_choise)} is less then Guessed  🤯\n")
                            else:
                                print(f"Your chosen {int(user_choise)} is Greater then Guessed  🤯\n")
                            print(f"only {min_chance - trying} tries left :".center(80, "-"))
                            user_choise = float(input("Wrong guessed! \n try again :"))
                        else:
                            print("Good luck Next time 😢:")
                            print(f"The Value is {randam} 😞")
                            break
                    else:
                        print(f"\nCongratulation you guessed correct in {trying + 1} Try 🥰:".title())
                        print("lets play again".title().center(80, '-'))


class UstbData:        # AlL university data is managed Here
    class PastPaper:   # This class is for past papers
        @staticmethod
        def semester1st():
            papers = ["CAG : 👉 https://drive.google.com/file/d/1QmCab5m-YN__GNKcX8TbpSq8KNkX_NyB/view?usp=drive_link",
                      "Functional English 👉 https://drive.google.com/file/d/1QqfD_KF9v9IJwyfI8YnTSSVqVyelzAvB/view?usp=drive_link",
                      "ICT :  👉 https://drive.google.com/file/d/1QoCPHAO-0RaCeYRPDPH7ENoEW0x_yQkJ/view?usp=drive_link",
                      "Islamic Study : 👉 https://drive.google.com/file/d/1QweBTrWVUZf4AOukzxOanxKTE2l-NLr9/view?usp=drive_link",
                      "Natural Science : 👉 https://drive.google.com/file/d/1QlAYEnpgldaQJ_Uub2DhyEtCZDwcUmpy/view?usp=drive_link",
                      "Programming : 👉  https://drive.google.com/file/d/1QpZiduk4LN0c-uK-Z_ZI3EiveBFpKJWA/view?usp=drive_link"]
            print("\n".join(papers))

        @staticmethod
        def semester2nd():
            papers = ["DLD :  👉  https://drive.google.com/file/d/1R1dLJJr2-u3NXXNJgRC3Ta2FiwA4mU6m/view?usp=drive_link",
                      "Expository Writting : 👉   https://drive.google.com/file/d/1QzlD9OWzw3p48kJFqWjG_MpQDV7XvgQd/view?usp=drive_link",
                      "ICP : 👉   https://drive.google.com/file/d/1R2rnZ-C8EE7ngB-eaUuicyN8xfB51dXD/view?usp=drive_link",
                      "MVC : 👉  https://drive.google.com/file/d/1QziauPLQHemRg-Y26_zRcU0IVVsMz5gi/view?usp=drive_link",
                      "QR :  👉  https://drive.google.com/file/d/1R6JDo4kn861EKmW4ZE8eYZUOfhbFttk2/view?usp=drive_link"]
            print("\n".join(papers))

        @staticmethod
        def semester3rd():
            print("3rd semester past papers will be Upload soon :")

    class Notes:# This class is for notes
        @staticmethod
        def semester1st():
            print("1st semester Note will be Upload Soon :")
        @staticmethod
        def semester2nd():
            print("1st semester Note will be Upload Soon :")
        @staticmethod
        def semester3rd():
            print("1st semester Note will be Upload Soon :")



    class Assignment:
        @staticmethod
        def semester1st():
            print("1st semester assignment will be Upload Soon :")

        @staticmethod
        def semester2nd():
            print("1st semester assignment will be Upload Soon :")

        @staticmethod
        def semester3rd():
            print("1st semester assignment will be Upload Soon :")


class ChatBot:
    def __init__(self):
        print('I am Exam Bot Coded By Waqar Afridi \U0001F92A.\nYou Can Ask Any Question Releted To Your Exam \U0001F644 .')
        while True:
            user = input("Ask Question:")
            print("wait Am thinking.... \U0001F914")
            response = call_gpt("define for exam paper without example and analogy and always used sample and easiest words and sentences:" + user)
            print(response)
            print("\nlets Understand with Example \U0001F447\n")
            response1 = call_gpt("use easiest words and sentance and give just example for --> " + user)
            print(response1)
            print("\nlets Understand with Analogy \U0001F447\n")
            response2 = call_gpt("use easiest words and sentance and just analogy for --> " + user)
            print(response2)





if __name__ == "__main__":
    print(f"𝕊𝕒𝕝𝕠𝕞 \U0001F44B !!!\nᴛʜɪs ᴘʀᴏɢʀᴀᴍ ᴄᴏᴅᴇᴅ ʙʏ ᴄᴏᴅᴇᴢᴅᴀᴋᴀ-ᴜsᴛʙ ᴛᴇᴀᴍ 🥰\n{version}\n{develper}\n")
    main()