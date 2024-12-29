import random
name=input("Enter your name")
rannum=random.randint(1,10)
print(f"{name}, This is a guessing game of numbers between 1 and 10")
num=int(input(f"{name}, enter a number "))
if num>=1 and num<=10:
    for i in range (1,4):
        if num<rannum:
            print(f"{name} ,It is too low")
        elif num>rannum:
            print(f'{name}, It is too high ')
        elif num==rannum:
            print(f"{name}, you won the game ")
            break
        if i<3:
            num=int(input(" Enter a number "))      
    else:
            print(f"You loss ! \nYou have finished your chance the correct answer was {rannum}.")
else:
    print(f"{name},Enter the number within the restricted input ")













