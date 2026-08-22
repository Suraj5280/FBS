for i in range(4):
    print(" " * (3 - i), end="")

    num = 1

    for j in range(i + 1):
        print(num, end=" ")

        num = num * (i - j) // (j + 1)

    print()


#   1
#  1 1
# 1 2 1
#1 3 3 1 