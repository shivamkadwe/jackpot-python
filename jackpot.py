import random
x = random.randint(1,101);
print(x)
print("=================")
print("Hard   = 1")
print("Medium = 2")
print("Easy   = 3")
print("=================")
option = int(input("Choose Option:"));
if (option==1):
    a=6
elif (option==2):
    a=11
elif (option==3):
    a=16
else:
    print("Enter correct input...")
for i in range(1,a):

    y = int(input("GUESS THE JACKPOT NUMBER :"))
    if (y<x):
        print("Enter the greater number...")
    elif(y>x):
        print("Enter the lower number...:")
    elif (y==x):
        print("YOU HAVE WON CHAMPION !")
        break

print("Play again")

