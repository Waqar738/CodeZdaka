question=[
    [
        ["what is your name :"],
        ["waqar","ahmad","afridi","khan"],
        [1]
    ],
    [
        ["most popular langage :"],
        ["java","python","C++","js"],
        [2]
        
    ]
]
totalmoney=0
for x in range(0,len(question)):
    print(f"{question[x][0][0]}\n")
    print(f"1:{question[x][1][0]}             2:{question[x][1][1]}")
    print(f"3:{question[x][1][2]}             4:{question[x][1][3]}\n")
    ans=int(input("Enter your answer between 1-4 :"))
    while(ans<1 or ans>4):
        ans=int(inpu t("Please answer should be between 1-4 :"))
    if ans==question[x][2][0]:
        totalmoney=1000*(x+1)
print(f"\nYour earned Rs= {totalmoney} PKR\n")

