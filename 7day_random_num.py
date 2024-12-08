import random
x=random.randint(1,100)
#print(x)
count = 0
user = 0
while user!=x:
    user=int(input("please ! guess a number "))
    count+=1
    if user>x:
        print(f"{user} is too high")
    elif user<x:
        print(f"{user} is too low")
    else:
        print("you won ")
        print(f"youve guessed the number {user} in {count} attempts.")