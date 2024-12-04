marks = input("enter your marks  ")
marks=int(marks)
print("your marks is ",marks)
#print(type(marks))
if marks>=30 and marks <=50:
    print("yor are just pass")
elif marks >= 51 and marks <=60:
    print("you are in  third position")
elif marks >=61 and marks <= 70:
    print("you are in second position")
elif marks >= 71 and marks<=100:
    print("first division ")
elif marks < 30:
    print("you are fail")
else:
    print("wrong input")
