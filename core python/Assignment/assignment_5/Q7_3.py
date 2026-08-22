n = int(input("Enter number of terms: "))

sum = 0
term = 1

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum =", sum)


#Geometric Series from 1 to n, Common Ratio = 2
#ex:2,4,6,8,10