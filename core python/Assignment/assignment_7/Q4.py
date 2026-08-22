n = 5

for i in range(1,n+1):
    for j in range(n-i):
        print("  ",end="")

    for j in range(i,2*i):
        print(j,end=" ")

    for j in range(2*i-2,i-1,-1):
        print(j,end=" ")

    print()

#        1 
#      1 2 1 
#    1 2 3 2 1 
#  1 2 3 4 3 2 1 
#1 2 3 4 5 4 3 2 1 