def prime(n,i):
    if(i == n):
        return True
    elif(n % i == 0):
        return False
    else:
        return prime(n,i+1)

n = int(input("Enter number: "))

if(n < 2):
    print("Not Prime")
elif(prime(n,2)):
    print("Prime Number")
else:
    print("Not Prime")