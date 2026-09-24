def infinite():
    i=1
    while(True):
        yield i
        i+=1

res = infinite()

#for i in res:
#    print(i)