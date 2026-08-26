li = [10,20,30,40,50,60,70,80,90,100]

print(li[0:5])          #to print from 0 to 5
print(li[2:8])          #to print from 2 to 8
print(li[:7])           #to print 0 to 7 (we can leve it blank if we want to print from starting of list)
print(li[:7:3])         #to print from 0 to 7 but with skiping numbers in beetwen (septs) after 3rd ':' colan it gets 'steps' to skip numbers in 
                                                                                                                                        #beetwen
print(li[4:])           #to print from 4 to 7 end of list
print(li[:])            #to print the whole list
print(li[::])           #to print the whole list (leveing the steps sectin blank will result it in taking default number which is 1) so it will 
                                                #print the whole list with skiping 1 number each time.
print(li[4:0:-1])       #to print list from 4 to 0 in revers(-1 used to revers the list)
print(li[::-1])         #directly print the whole list in revers
print(li[8::-4])        #print only 90,50,10 use -4 as step to pirint the sting with 3 numbers skiping each time
print(li[9::-3])        #testing