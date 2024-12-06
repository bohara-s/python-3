
num= int(input("enter the number to check prime or compsite num "))
print("the given number is ",num,)
s= 1 
c= 0

while s<=num:
    r=num%s
    if r==0:
        c=c+1
    s=s+1
 

if c>2:
    print(" it is composite number")
else:
    print("it is  prime number")  