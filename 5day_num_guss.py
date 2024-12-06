# for_reapet="a"
# while for_reapet=="y": 
print("Welcome to the Number Guessing Game!")
import random
x = random.randint(1,100)
count = 0
y=0
while x!=y:
        y = int(input("please ! guess a number "))
        count +=1
        if x>y:
            print("too low ")
        elif x<y:
            print("too high")
    
        else:
            print(f"Congratulations! You've guessed the number {x} in {count} attempts.")

   # for_reapet=input("do you want to play again (y/n)")
