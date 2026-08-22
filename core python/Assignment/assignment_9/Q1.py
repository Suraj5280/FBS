def fact(n):
    if(n == 0):
        return 1
    else:
        return n * fact(n-1)

def sum(n):
    if(n == 0):
        return 0
    else:
        return fact(n) + sum(n-1)

n = int(input("Enter n: "))

print("Sum =",sum(n))