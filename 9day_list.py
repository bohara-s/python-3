# lst1= ['a','b','c']
# print(lst1)
# print(lst1[1],"for")


# a=3 
# int= 8
# list1=['ball','apple',99,'sushil',3.33]
# print(list1[4])
# print(list1[3])
# print(list1[2])
# print(list1[1])
# print(list1[0])

# print(list1[4:0:-1])




# list1 .append('cat')
# print(list1)



# lst2=list((2,3,'sushil','bohara'))
# print(lst2)
# print(lst2[3:0:-1])
# print(lst2)





# #access list item using loop

# for i in list1:
#     print(i,end=",")
    
    
    
#wap to remove duplicate item from list[ ball , cat ball 5 7 5]
lst3 = [ "ball" , "cat", "ball" ,"5", "7" ,"5"]
lst4=[]
for i in lst3:
    if i in lst4:
        continue
    else:
        lst4.append(i)
print(lst4)
    