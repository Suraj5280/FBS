n = 5

for i in range(1,n+1):
    for j in range(n-i):
        print("  ",end="")

    print(1,end=" ")

    if(i > 1):
        if(i == n):
            for j in range(2,i+1):
                print(j,end=" ")
        else:
            print(i,end=" ")

    print()





#        1
#      1    2
#    1        3
#  1            4
#1   2   3   4   5   