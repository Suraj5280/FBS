def fact(n):
    f = 1

    for i in range(1,n+1):
        f = f * i

    return f

def sum(n):
    s = 0

    for i in range(1,n+1):
        s = s + fact(i)

    return s

n = int(input("Enter n: "))

print("Sum =",sum(n))