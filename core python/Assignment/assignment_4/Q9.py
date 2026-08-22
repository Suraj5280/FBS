start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
num = int(input("Enter the number: "))

for i in range(start, end + 1):
    if i % num == 0:
        print(i)



#print number divisable from user given number with user given range
#for range(star,end) to take rang
#if i%num==0 to check if number divisible