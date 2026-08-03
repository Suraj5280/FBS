num = int(input('enter a number:'))
if(num<=0):
    print('number is lees than 0')
elif(num<=50):
    print('number is between 1-50')
elif(num<=100):
    print('number is between 51-100')
elif(num<=150):
    print('number is between 101-150')
elif(num<=250):
    print('number is between 151-250')
else:
    print(f'{num} is grater than 250')