start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start,end+1):
    temp = n
    digits = 0

    while(temp > 0):
        digits = digits + 1
        temp = temp // 10

    temp = n
    sum = 0

    while(temp > 0):
        digit = temp % 10
        sum = sum + digit ** digits
        temp = temp // 10

    if(sum == n):
        print(n)


#armstrong number chaking within user difind range