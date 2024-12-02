#string manupulation
"""
firsi_name ="shyam"
second_name ="ram"
print(firsi_name+second_name)   # concat


a="ram"
b = 9
print(a+str(b))

first_sentence ="       hello i am from sindhpalchok "
print(first_sentence.strip())#strip() it remove unwanted space
sushil_bohara = "sushilbohaar@gmail.com"
splitted_data = sushil_bohara.split('@')
print(splitted_data)


about_nepal = "nepal is ...nepal .... kahsiudqe alasdkqpqoei india...issja ...india"
correct_data = about_nepal.replace('india','nepal')#replace is used to replace old to new
correct_data = correct_data.replace('.','the')
print(correct_data)

"""
father_name = "Hello, and Welcome To my world"
print(father_name.upper())#all capatalize
print(father_name.capitalize())#capatalize first letter
print(father_name.title())#capatlize first character
print(father_name.casefold())#Converts string into lower case small letter
print(father_name.center(100))#Returns a centered string
print(father_name.islower())#Returns True if all characters in the string are lower case
print(father_name.index("world"))#Searches the string for a specified value and returns the position of where it was found
print(father_name.isspace())#Returns True if all characters in the string are whitespaces	
print(father_name.zfill(40))#Fills the string with a specified number of 0 values at the beginning
print(father_name.strip())#Returns a trimmed version of the string
print(father_name.len(father_name))