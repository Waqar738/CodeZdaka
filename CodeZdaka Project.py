import random
import math
from ai import call_gpt

develper = "ᵇʸ 𝕎𝕒𝕢𝕒𝕣 𝔸𝕗𝕣𝕚𝕕𝕚"
version = "𝕍𝕖𝕣𝕤𝕚𝕠𝕟 𝟚.𝟘"


def main():
    aval_feature = [
        [1, 2, 3,4],
        ["Uni Data", "Games", "Chat Bot","Courses"],
        [ustbdatakarel, gameskarel, chatbotkarel,courseskeral]
    ]
    tabulate(["ID", "Feature"], list(zip(aval_feature[0], aval_feature[1])))
    user_input = int(input("ꜱᴇʟᴇᴄᴛ ꜰᴇᴀᴛᴜʀᴇ ʙʏ ɪᴅ :".title()))
    while user_input not in aval_feature[0]:
        user_input = int(input("ᴘʟᴇᴀsᴇ sᴇʟᴇᴄᴛ ᴄᴏʀʀᴇᴄᴛ ɪᴅ :".title()))
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
    user_input = int(input("Sᴇʟᴇᴄᴛ Dᴀᴛᴀ ʙʏ ɪᴅ :".title()))
    while user_input not in data[0]:
        user_input = int(input("ᴘʟᴇᴀsᴇ sᴇʟᴇᴄᴛ ᴄᴏʀʀᴇᴄᴛ ɪᴅ :".title()))
    chosen_data = data[2][user_input-1]
    # chosing semester ....
    semester = [
        [1, 2, 3],
        ["1st semester", "2nd semester", "3rd semester"],
        [chosen_data.semester1st, chosen_data.semester2nd, chosen_data.semester3rd]
    ]
    tabulate(["ID", "Semester"], list(zip(semester[0], semester[1])))
    user_input = int(input("Sᴇʟᴇᴄᴛ sᴇᴍᴇsᴛᴇʀ ʙʏ ɪᴅ :".title()))
    while user_input not in data[0]:
        user_input = int(input("ᴘʟᴇᴀsᴇ sᴇʟᴇᴄᴛ ᴄᴏʀʀᴇᴄᴛ ɪᴅ :".title()))
    print("ᴅᴏᴡɴʟᴏᴀᴅ ꜰʀᴏᴍ ʙᴇʟᴏᴡ Gᴏᴏɢʟᴇ Dʀɪᴠᴇ ʟɪɴᴋs \U0001F447 :")
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

def courseskeral():
    courses()

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
            papers = ["DLD : 👉 https://drive.google.com/file/d/1R1dLJJr2-u3NXXNJgRC3Ta2FiwA4mU6m/view?usp=drive_link",
                      "Expository Writting : 👉 https://drive.google.com/file/d/1QzlD9OWzw3p48kJFqWjG_MpQDV7XvgQd/view?usp=drive_link",
                      "ICP : 👉 https://drive.google.com/file/d/1R2rnZ-C8EE7ngB-eaUuicyN8xfB51dXD/view?usp=drive_link",
                      "MVC : 👉 https://drive.google.com/file/d/1QziauPLQHemRg-Y26_zRcU0IVVsMz5gi/view?usp=drive_link",
                      "QR : 👉 https://drive.google.com/file/d/1R6JDo4kn861EKmW4ZE8eYZUOfhbFttk2/view?usp=drive_link"]
            print("\n".join(papers))

        @staticmethod
        def semester3rd():
            papers = ["DataBase  : 👉 https://drive.google.com/file/d/1S7Y373ZRKcUni98b_sivq-uGMmlv5l8C/view?usp=drive_link",
                      "Entrepreneureship : 👉 https://drive.google.com/file/d/1S9gqIrQjPBLp3BqkApj2kEpic6FGA57d/view?usp=drive_link",
                      "Linear Algebra : 👉 https://drive.google.com/file/d/1S8abkAKWZDuH0Hela6MkDH2sVU-4bwRm/view?usp=drive_link",
                      "Statistic : 👉 https://drive.google.com/file/d/1SCoxGidHwPqQDG-U_dwPIzU8okQYsdRA/view?usp=drive_link",]
            print("\n".join(papers))

# This class is for notes
    class Notes:
        @staticmethod
        def semester1st():
            print("1st semester Note will be Upload Soon :")
        @staticmethod
        def semester2nd():
            notes = ["English :  👉https://drive.google.com/file/d/1Si3lYhX6z8MQw-hKu7k55NvlwXrKakLL/view?usp=drive_link"

            ]
            print("\n".join(notes))
        @staticmethod
        def semester3rd():
            notes = [
                "Civic :  👉 https://drive.google.com/file/d/1SNLGMHQjeR5bciWNx0E9nZiB0P5_17bp/view?usp=drive_link",
                "DataBase :  👉 https://drive.google.com/file/d/1SLsN54NJtbclF9yJ3eqAcC9_3VhaiWSE/view?usp=drive_link",
                "Entrepreneureship :  👉 https://drive.google.com/file/d/1SICxjYz34micfcJBvl7t3urcMNnuYOdi/view?usp=drive_link",
                "Linear Algebra :  👉 https://drive.google.com/file/d/1SPTr0_rKa8GIR9F_zlopHiDt0rd02mjY/view?usp=drive_link",
                "Management :  👉 https://drive.google.com/file/d/1SRjEHSvlBtYDD_Xen247XTupvFYrCGZi/view?usp=drive_link",
                "Statistic :  👉 https://drive.google.com/file/d/1SIpZfxhHyJoCPUHNiYYiagBn1gix0vcy/view?usp=drive_link",
                "T&B Writing :  👉 https://drive.google.com/file/d/1SVYh7_pPpZwfVpyYA_oIO6-6h9RoveEn/view?usp=drive_link"
            ]
            print("\n".join(notes))



    class Assignment:
        @staticmethod
        def semester1st():
            print("1st semester assignment will be Upload Soon :")

        @staticmethod
        def semester2nd():
            assign = ["DLD mid Exam : 👉 https://drive.google.com/file/d/1T4yMPVWwTZSrx7OJmzWAobRGYLEtGs3z/view?usp=drive_link",
                      "DLD part 2 : 👉 https://drive.google.com/file/d/1StgmTQpsCRLG-Imb0TZsuQ-G3H6ZkDav/view?usp=drive_link",
                      "DLD part 1 : 👉 https://drive.google.com/file/d/1T-WhVR1t5Uq9lhuLJVxNgJvqhJZ0_Z-n/view?usp=drive_link",
                      "English : 👉 https://drive.google.com/file/d/1Ss6dqZ9AF-7DFvyjEBXBzPddiuKLR3TA/view?usp=drive_link",
                      "ICP Mid Exam : 👉 https://drive.google.com/file/d/1SnC6IlUm6xANOeTwVuu-KW0STid6dzPs/view?usp=drive_link",
                      "ICP : 👉 https://drive.google.com/file/d/1Sm4qzlGLdiGwxJXozR4Dsv-pWiLdfcBl/view?usp=drive_link",
                      "Math Mid Exam : 👉 https://drive.google.com/file/d/1SiLv8GBLqAvE2IrJSCyWlsyhO-HEofeE/view?usp=drive_link",
                      "MVC : 👉 https://drive.google.com/file/d/1SkbX7dQg_v3awjSeBfwrllQj9sbExl-_/view?usp=drive_link",
                      "OOP Mid Exam : 👉 https://drive.google.com/file/d/1SxPssyjk17zuYYglvOvTqvd77FUi3fL9/view?usp=drive_link",
                      "QR : 👉 https://drive.google.com/file/d/1Sozf0_zBbB4laW_LLcPWUfB8suv-fTKJ/view?usp=drive_link"
            ]
            print("\n".join(assign))

        @staticmethod
        def semester3rd():
            assign = ["Linear Algebra Final : 👉 https://drive.google.com/file/d/1T8-GM4Mu-XfEoNpsQVdXg035IP3KME2a/view?usp=drive_link",
                      "Linear Algebra Mid : 👉 https://drive.google.com/file/d/1T5nR5e4enwOTDo3BwFyfa40g6Nk-nvXp/view?usp=drive_link"
            ]


class ChatBot:
    def __init__(self):
        print('ɪ ᴀᴍ ᴇxᴀᴍ ʙᴏᴛ ᴄᴏᴅᴇᴅ ʙʏ ᴡᴀǫᴀʀ ᴀғʀɪᴅɪ \U0001F92A.\nʏᴏᴜ ᴄᴀɴ ᴀsᴋ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴ ʀᴇʟᴇᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴇxᴀᴍ \U0001F644 .')
        while True:
            user = input("ᴀsᴋ ԛᴜᴇsᴛɪᴏɴ:")
            print("ᴡᴀɪᴛ ᴀᴍ ᴛʜɪɴᴋɪɴɢ.... \U0001F914")
            response = call_gpt("define for exam paper without example and analogy and always used sample and easiest words and sentences:" + user)
            print(response)
            print("\nʟᴇᴛs ᴜɴᴅᴇʀsᴛᴀɴᴅ ᴡɪᴛʜ ᴇxᴀᴍᴘʟᴇ \U0001F447\n")
            response1 = call_gpt("use easiest words and sentance and give just example for --> " + user)
            print(response1)
            print("\nʟᴇᴛs ᴜɴᴅᴇʀsᴛᴀɴᴅ ᴡɪᴛʜ ᴀɴᴀʟᴏɢʏ \U0001F447\n")
            response2 = call_gpt("use easiest words and sentance and just analogy for --> " + user)
            print(response2)


class courses:
    def __init__(self):
        course = ["①𝗔𝘄𝗳𝗲𝗿𝗮 𝗔𝗟𝗠𝗦 : https://awferalms.com/ \nOꜰꜰᴇʀs \U0001F447\n➔ ᴘʏᴛʜᴏɴ ᴘʀᴏɢʀᴀᴍɪɴɢ \n➔ Dᴀᴛᴀ Sᴄɪᴇɴᴄᴇ\n➔ Mᴀᴄʜɪɴᴇ ʟᴇᴀʀɴɪɴɢ \n➔ Dᴇᴇᴘ ʟᴇᴀʀɴɪɴɢ ᴇssᴇɴᴛɪᴀʟs\n➔ ɴʟ ᴘʀᴏᴄᴇssɪɴɢ",
                  "②(𝗖𝗜𝗣) 𝗦𝘁𝗮𝗻𝗳𝗼𝗿𝗱 𝘂𝗻𝗶𝘃𝗲𝗿𝘀𝗶𝘁𝘆 : 👉 https://codeinplace.stanford.edu/ \nOꜰꜰᴇʀs \U0001F447\n➔ ᴘʏᴛʜᴏɴ ᴘʀᴏɢʀᴀᴍɪɴɢ"]
        print("\n\n+=====+=====+=====+=====+\n\n".join(course))
        # print("Cᴏᴍᴘᴜᴛᴇʀ ʀᴇʟᴀᴛᴇᴅ ᴄᴏᴜʀsᴇs ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ sᴏᴏɴ , sᴏ sᴛᴀʏ ᴛᴜɴᴇᴅ !")




if __name__ == "__main__":
    print(f"𝕊𝕒𝕝𝕠𝕞 \U0001F44B !!!\nᴛʜɪs ᴘʀᴏɢʀᴀᴍ ᴄᴏᴅᴇᴅ ʙʏ ᴄᴏᴅᴇᴢᴅᴀᴋᴀ-ᴜsᴛʙ ᴛᴇᴀᴍ 🥰\n{version}\n{develper}\n")
    main()
    print("ᴛʜᴀɴᴋs ꜰᴏʀ ᴜsɪɴɢ — 🥰\nᴘʟᴇᴀsᴇ ʀᴇᴘᴏʀᴛ ᴘʀᴏʙʟᴇᴍ ᴏʀ ᴍɪssɪɴɢ ᴅᴀᴛᴀ ᴛᴏ \U0001F447 ᴛᴏ ʙᴇ ᴀᴅᴅ\n+923126565549")