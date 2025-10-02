'''
1 for snake 
-1 for water
0 for gun
'''
import random


computer = random.choice([-1,0,1])
youstr= input("Enter your choice: ")
youDict ={"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake",-1: " Water", 0:" Gun" }

you =youDict[youstr]

print(f"you chose {reverseDict[you]}\nComputer chose{reverseDict[computer]}")
if(computer==you):
    print("Tied Up!")
else:    
    if(computer== -1 and you==1):
        print("You Win!")
    elif(computer== -1 and you==0):
        print("You Lose!")
    elif(computer== 1 and you==-1):
        print("You Lose!")
    elif(computer== 0 and you==-1):
        print("You Win!")
    elif(computer== 1 and you== 0):
        print("You Win!")
    elif(computer== 0 and you==1):
        print("You Lose!")
    else:
        print("Somthings gone wrong!!!")