gender = input('enter gender(M/F)')
age = int(input('Enter age:'))

if(gender == 'F'):
    if(age >= 18 ):
        print('girl is eligible for marriage')
    else:
        print('not eligible')
else:
    if(age >= 21):
        print('boy is eligibel')
    else:
        print('not eligible')