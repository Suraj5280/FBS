#1 pass: to neglect expected idented error
#for i in range(1,10):
 #   pass

#2 breack:to stop the loop
#for i in range(1,10):
 #   if(i == 3):
  #      break
   # print(i)


#3 continue:to stop current iteration
#for i in range(1,10):
 #   if(i=3):
  #      continue
   # print(i)


#4 else:to execute at end of the loop(if use continue keyword else will execute / but if used
#break keyword else will not execute)
#for i in range(1,10):
 #   if (i==5):
  #     continue
   # print(i)
#else:
 #   print('else executed')


#example Q

num = int(input('enter a number:'))

for i in range(2,num):
    print(i)
    if(num % i == 0):
        print(f'{num} 15 is not prime')
        break
else:
    print(f'{num} is a prime number')