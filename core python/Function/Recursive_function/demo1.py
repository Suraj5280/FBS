def series(n):
    if(n > 0):          # to stop from looping infinitely
        print(n)
        series(n - 1)  #to substract 1 each time

series(5)       #to print