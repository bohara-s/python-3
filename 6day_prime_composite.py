x=int(input("enter renge"))
num = 2
while num<=x:
    c=0
    s=1
    while s<=num:
        if num %s==0:
            c=c+1
        s=s+1
    if c==2:
        print(f"{num} is prime")
    else:
        print(f"{num} is composite")
    num=num+1