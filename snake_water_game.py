import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (snake/water/gun): ")
youDict = {
    "snake": 1,
    "water": -1,
    "gun": 0
}

if youstr in youDict:
    you = youDict[youstr]
else:
    print("Invalid input!")
    exit()

print(f"Computer chose: {list(youDict.keys())[list(youDict.values()).index(computer)]}")

if computer == you:
    print("It's a tie")
elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
    print("You win")
else:
    print("You lose")
