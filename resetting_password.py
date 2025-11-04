password_1 = "Hello123"
password_2 = "Hello123"

if password_1 == password_2:
    print("Password Changed")
else:
    if password_1.casefold() == password_2.casefold():
        print("Check the cases and try again")
    else:
        print("password dont match")