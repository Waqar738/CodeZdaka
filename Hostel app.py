hostel = {
    'room 1': [
        'ahmad',
        'ali'
    ],
    'room 2': [
        'khan',
        'afridi'
    ],  
    'room 3': [
        'zeshan',
        'ibrar'
    ]
}
user_room = input("Enter Room No# :")  # room number taken form user
while not user_room.isnumeric():
    user_room = input("Enter Room No# (1,2,...) :")  # room number taken form user in digit
else:
    while user_room != 'ok':
        room = [x for x in hostel if user_room in x]  # checked room registration is done or not.
        if len(room) == 0:
            print(f"The Room {user_room} is Not register yet :".title())
            user_ch = input("are you want to register ? (yes/No) :".title()).lower()  # user want to add room or not
            while user_ch != 'yes' and user_ch != 'no':
                user_ch = input('please only yes or no :'.title()).lower()
            if user_ch == 'no':
                exit()
            elif user_ch == 'yes':
                first_std = input("Enter 1st student :".title()).title()
                second_std = input("Enter 2nd student :".title()).title()
                add_std_list = [first_std, second_std]
                hostel.setdefault(f"room {user_room}", add_std_list)
                print(f"Room no# {user_room} is allowted to ",hostel[f"room {user_room}"])
            else:
                pass
        else:
            print(hostel.get(room[0]))

        user_room = input("Enter Room No# :")