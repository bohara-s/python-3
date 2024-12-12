# # text = 'hello, my name is sandesh'
# # #print(text.index("name"))
# # x=text[5]
# # print(x)

# #WAP to take a input from the user and make different list for different user.    

# number=int(input("Enter the number of people: "))    

# i=1    

# list_third=[]    

    

# while i<=number:    

#     list_second=[] #Reset list_second for each user    

#     print(f"For user {i}")    

#     list_second.append(input(f"Enter the Name : "))    

#     list_second.append(input(f"Enter the Age: "))    

#     list_second.append(input(f"Enter the Address "))     
#     list_third.append(list_second)    

#     i+=1    
# print(list_third)

dict1 = []  # List to store student data
x = int(input("Enter the number of students: "))  # Get the number of students

# Check if the input is a valid number
if x <= 0:
    print("Number of students must be greater than 0")
else:
    for i in range(0, x):  # Loop through the number of students
        name = input(f"{i+1} Enter Student name: ")
        # Collect marks and convert them to integers
        math_mark = input(f"Enter {name}'s Math mark: ")
        science_mark = input(f"Enter {name}'s Science mark: ")
        social_mark = input(f"Enter {name}'s Social mark: ")
        nepali_mark = input(f"Enter {name}'s Nepali mark: ")
        english_mark = input(f"Enter {name}'s English mark: ")

        # Append the student data to the list inside the loop
        dict1.append({
            'name': name,
            'math_mark': math_mark,
            'science_mark': science_mark,
            'social_mark': social_mark,
            'nepali_mark': nepali_mark,
            'english_mark': english_mark
        })

    # Print all student data after the loop
    print(dict1)
