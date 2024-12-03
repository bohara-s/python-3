"""
a = 4  # Binary: 0100
b = 2  # Binary: 0010

result = a & b  # Bitwise AND
print(result)   # Output: 1 (Binary: 0001) 



a = 5
b = 10

print(a != b)  # Output: True (since 5 is not equal to 10)
print(a != 5)  # Output: False (since 5 is equal to 5)

"""


# condition
"""
there is three types of condition 
1) if
2) if else
3) if .. elif....elif....else...
"""
"""
age = 13 
if age > 18:
    print("you can  vote ")


# syntax  
# if condittion true:
#      statements


age = 21 
if age > 20:
    print(" you can  marry")


# syntax 
# if condition true:
#     statements
# else:
#     statements


age = 20 
if age > 20:
    print("you can vote ")
else:
    print ("you can not vote ")
    """

# wap to 

"""
age = 20 
if age > 0:
    print(" you are child ")
if age > 13:
    print(" you are aadult ")
if age >20 :
    print("you are old man ")

"""



age = 25
if age.isdigit():
    print("wrong input ")
elif age > 0 and age <13:
    print ("you are cild")
elif age > 13 and age <20:
    print("you are adualt ")
elif age > 20 and age < 100:
    print("you are old man ")
elif age < 0 and age <100:
    print("wrong input ")

else:
    print("dfdf")

