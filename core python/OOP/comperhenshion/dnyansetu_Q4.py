#add 10 to each odd number in list

li=[10,2,3,4,7,11,33]
new=[]
for i in li:
    if(i%2!=0):
        new.append(i+10)
print(new)


#with comperhenshion

li=[10,2,3,4,7,11,33]
new=[i+10 for i in li if (i%2!=0)]
print(new)
