#wap to add 2 in your given list.

#regular method

li=[1,2,3,4,5,]
for i in range(len(li)):
    li[i]=li[i]+2
print(li)



#comprehension method

li=[1,2,3,4,5]
li=[x+2 for x in li]
print(li)