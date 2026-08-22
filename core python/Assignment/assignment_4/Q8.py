start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)


#number divisble by 7 and multipliable from 5 in a range