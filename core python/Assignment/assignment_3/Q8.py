import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "suraj" and password == "1234":
    captcha = random.randint(1000, 9999)
    print("Captcha =", captcha)

    entered = int(input("Enter captcha: "))

    if entered == captcha:
        print("Success")
    else:
        print("Failed")
else:
    print("Invalid User ID or Password")


# id,pass and captcha check program