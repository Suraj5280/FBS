num = int(input("Enter a 3-digit number: "))

if 100 <= num <= 999:
    if num == (num % 10) * 100 + ((num // 10) % 10) * 10 + num // 100:
        print("Palindrome")
    else:
        print("Not Palindrome")
else:
    print("Please enter a 3-digit number")


#same same but diffrent
#("palindrome" same from left to right and right to left) is the number pelindrome
#ex. 121 same from both sides