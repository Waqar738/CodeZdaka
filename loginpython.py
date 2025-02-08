################################################ user have entred their data ##############
username=input("Create youruser name :")
password=input("Create your password :")
################################################ now user have to login ###################
while(username==password):
    print("username and password should be different :")
    username=input("Create youruser name :")
    password=input("Create your password :")
else:
    print("\n you have to login now :\n")
    uncheck=input("Enter your username: ")
    while(uncheck != username):
        uncheck=input("Enter your correct username: ")
    else:
        pwcheck=input("Enter your password: ")
        if pwcheck != password:
            for i in range(1,5):
                pwcheck=input("Enter your correct password: ")
                if pwcheck==password:
                    print("wellcome to login panel :")
                    break  
                else:
                    if i==2:
                        print("Your have last chance :")
                    if i==3:
                        print("Attampt Limit excesed, please try again :")
                        break
        else:
            pass