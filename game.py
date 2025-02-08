import math
print("Wellcome to play game, Here are three question : ")
yesno=input("Are you ready to play (Yes/No) :")
yesno.lower
marks=[]
    ####################### Function #####################################
def Question(Qn,Qns,Qs,Qa):
    print(Qns,Qs)
    Qn=input()
    Qn.lower
    if Qn==Qa:
        marks.append(20)
    else:
        marks.append(0)
    ##########################2nd function ########################################
def answerout(QN,Qa):
    print(f"{QN} answer is --> {Qa}")

    ####################### end of function #######################################
while(yesno!="yes") and (yesno!="no"):
    yesno=input("Please answer should be in yes or no :")
else:
    if yesno=="yes":
        print("wellcome to game lubby :\n")
        ##################### all questions  ##################################
        Question("Q1","Question no 1 :","Is 'wakar' is a correct ?","no")
        Question("Q2","Question no 2 :"," write correct spill of queston 1 :","waqar")
        Question("Q3","question No 3 :"," is waqar is a Name of person ?","yes")
        ##################### result calculation #########################
        tmarks=sum(marks)
        resultout=input("are you want to see your result :")
        resultout.lower
        if resultout=="yes":
            answerout("Q1","No")
            answerout("Q2","waqar")
            answerout("Q3","Yes")
            print(f"Your totall marks is {tmarks}")
        else:
            print("But i still show your result \U0001F923:")
            answerout("Q1","No")
            answerout("Q2","waqar")
            answerout("Q3","Yes")
            print(f"Your totall marks is {tmarks}")
    else:
        print("Okay Good luck! you can try next time :")