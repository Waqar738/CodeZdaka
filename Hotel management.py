import datetime
totall_price=0
selected_items=[]
number_of_items=0
eat_timing = ''
# Hotel is total menu list of all time food :
class Hotel:
    def __init__(self):
        self.danner_menu = {
            "Bannu Pulao": [150,1, True],
            "Keema": [250, 2, True],
            "Nihari": [300, 3, True],
            "Biryani": [150, 4, True],
            "Lobia": [100, 5, True],
            "Chicken": [200, 6, True]
        }
        self.lunch_menu = {
            "Bannu Pulao": [150, 1, True],
            "Karahi": [250, 2, True],
            "Nihari": [300, 3, True],
            "Biryani": [150, 4, True],
            "Daal Mash": [100, 5, True],
            "Chicken": [200, 6, True]
        }
        custmer_data = dict()

# def user_order():
#     user_input = list(input("Select the item by their id to order :".title()))
#     print(user_input)
    

def show_menu(take_menu):       #printing menu in design format according to time ...... called in
    items_list = list(take_menu.keys())
    price_list = [take_menu[x][0] for x in items_list]
    items_id_list = [take_menu[x][1] for x in items_list]
    print(" MENU ".center(50, '*'))
    print(f'\nITEM_ID'.ljust(16,' '),f'FOOD_ITEMS'.ljust(14,' '),f'PRICE '.center(13,' '))
    for x,y,z in zip(items_list,price_list,items_id_list):
        print(f'{z}  -->'.ljust(11,' '),f'|   {x}'.ljust(15,' '),f'|    PKR : {y}')
    print(''.center(50, '*'))

def menu_choseing():       #checking time and their menu .... called in ' wellcome fun '.....
    ampm =int(datetime.datetime.now().strftime('%H'))
    if ampm >= 10 and ampm <= 14:
        global eat_timing
        show_menu(Hotel().lunch_menu)
        eat_timing = Hotel().lunch_menu
    elif ampm >= 18 and ampm <= 22:
        show_menu(Hotel().danner_menu)
        eat_timing = Hotel().lunch_menu
    else:
        print("the shop is currently closed:".title())


def custmer_details():
    custmer_name = input(" Enter Custmer Name :")
    menu_choseing()
    global selected_items
    user_input = [int(x) for x in input("select item by their id :") if x.isdigit()]
    user_input_ids = set([x for x in user_input if 0<x<=6])
    for x in user_input_ids:
        for y in eat_timing:
            if x == eat_timing[y][1]:
                selected_items.append(y)
    print(selected_items)
    

def wellcome():     #The first function to be called ......
    new_comer = input("are you here to order some food (yes / no) :".title()).lower()
    while new_comer != 'yes' and new_comer != 'no':
        new_comer = input("are you here to order some food : please-->(yes / no)".title()).lower()
    if new_comer == 'yes':
        custmer_details()
    else:
        print("okay thanks you for coming :".title())

wellcome()


