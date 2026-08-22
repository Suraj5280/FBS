n = 5

for i in range(1,n+1):
    print(1,end=" ")

    if(i > 1):
        for j in range(2,i):
            print(j,end=" ")

    if(i > 1):
        print(i,end=" ")

    print()



#1
#1  2
#1    3
#1      4
#1 2 3 4 5 