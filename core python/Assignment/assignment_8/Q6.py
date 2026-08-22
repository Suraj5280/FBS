def fib(n):
    a = 1
    b = 1

    for i in range(1,n+1):
        print(a,end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter number of terms: "))

fib(n)