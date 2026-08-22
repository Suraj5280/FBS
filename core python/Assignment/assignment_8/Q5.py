def prime(n):
    for i in range(2,n):
        if(n % i == 0):
            return False

    return True

def sumprime(n):
    s = 0

    for i in range(2,n+1):
        if(prime(i)):
            s = s + i

    return s

n = int(input("Enter n: "))

print("Sum =",sumprime(n))