li = [30,24,90,82,99,55,22,33]

max=li[0]               #to take the value.  (li[0] to start form 0 and go to end of list)

for ind in range(1,len(li)):        #define range (1,len(li)) used to access all the numbers in list.

    if(li[ind]>max):            #to check the bigger number.

        max=li[ind]             #to change the max valu with the newly found bigger number.

print('max is :',max)               #print max.