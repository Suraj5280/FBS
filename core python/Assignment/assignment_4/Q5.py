n = int(input("Enter n: "))

a = -1
b = 1

for i in range(1,n+1):
    c = a + b
    print(c,end = ' ')
    a = b
    b = c

#print Fibonacci series till n