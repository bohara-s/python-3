
dict1=[]
x = int(input("Enter a number of student  "))
#if not isinstance(dict1,int) or dict1 < x:
  #  print("wrong input")
#else:
for i in range(0,x):
    name=input(f"{i+1} Enter Student name  ")
    math_mark=input(f"Enter {name}'s Math mark ")
    science_mark=input(f"Enter {name}'s Science mark ")
    social_mark=input(f"Enter {name}'s Social mark ")
    nepali_mark=input(f"Enter {name}'s Nepali mark ")
    english_mark=input(f"Enter {name}'s English mark ")

    dict1.append({
    'name':name,
    'math_mark':math_mark,
    'science_mark':science_mark,
    'social_mark':social_mark,
    'nepali_mark': nepali_mark,
    'english_mark':english_mark
    })
print(dict1)