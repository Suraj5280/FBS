#write in words if the number is odd or even from list


#with regular method
li = [1,2,3,4,5,6,7]
odd_li=[]
for ele in li:
    if ele%2==0:
        odd_li.append('EVEN')
    else:
        odd_li.append("ODD")
print(odd_li)


#with comperhenshion