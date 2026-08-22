def sum(n):
    s = 0

    for i in range(1,n+1):
        s = s + i ** i

    return s

n = int(input("Enter n: "))

print("Sum =",sum(n))