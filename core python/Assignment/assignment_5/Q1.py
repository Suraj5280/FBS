correct_id = "suraj"
correct_password = "1234"

for i in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect ID or Password")

else:
    print("You have exceeded 3 attempts.")


# id,pass program but with only 3 attemps