
#print the natural numbeer 1 to 10 .....
"""
x=1,2,3,4,5,6,7,8,9,10
print(x)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

"""

"""

 #nature of variables
x="1234"#str
y="bohara"#str
z=123#int
print(x,y,z)
print( f"type of {x}  ",type(x))
print(f"type of {y}   ",type(y))
print(f"type of {z} ",type(z))
"""



#type casting
"""
age=22
salery=2.2
name= "bohara"
print(type(age))
print(type(salery))
print(type(name))

x=int(name)
y=float(age)
z=int(salery)


#type cating floating point to intiger value of salery
salery=12.33
print(type(salery))
salery=int(12.33)
print(salery)
print(type(salery))
"""
#operator 
"""
1,arthmatic operator    /   *   -   +
2,logical operator  and or  not
3,assignment  operator   =  
compression   operator <,>.>=,<=
bitwise  operator  =||
"""
"""
print(4+5)
print(5*5)
print(3//6)
print(5%2)
print(8-6)
x=2
y=4
print(f"sum of {x} and {y} is",x+y )
print(f"div of {x} and {y} is",x/y )
print(f"multi of {x} and {y} is",x*y )
print(f"sub of {x} and {y} is",x-y )
print(f"mod of {x} and {y} is",x%y )
"""

"""
# Default behavior
print("Hello")
print("World")
"""
"""
output

hello
world 

"""
"""

# Custom end parameter
print("Hello", end=" ")
print("World")
"""
"""
output 

hell oworld 

""" 
#example of AND gate 
 
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")
else:
    print("One or both conditions are false")

"""
output

Both conditions are true

"""

# for or gate

x = 5
y = 2
if x > 3 or y > 8:
    print("At least one condition is true")
else:
    print("Both conditions are false")

"""
output

At least one condition is true

"""

#for not gate

x = 5
if not(x > 10):
    print("x is not greater than 10")
else:
    print("x is greater than 10")
    """
    output

    x is not greater than 10
    
    """