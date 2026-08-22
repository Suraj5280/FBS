for i in range(1, 6):
    print(" " * (5 - i) * 2, end="")

    for j in range(2 * i - 1):
        print("* ", end="")

    print()

#        * 
#      * * * 
#    * * * * * 
#  * * * * * * * 
#* * * * * * * * * 