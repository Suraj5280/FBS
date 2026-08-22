#1. To pass multiple values to function
#2. Mention 1 astrisk symbole before parameter name in function defination
#3. Passed values are stored in tuple format
#4. Use for loop to iterate values from tuple

def add(*data):
    sum = 0
    for val in data:
        sum += val
    return sum

res=add(10,20,30,40,50,60,70,80,90,1,2,3,4,5,6,7,8,9)
print(res)