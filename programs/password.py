def password():
    pass

pwd = input("enter the string you want as a password : ")
if password(pwd):
    print("{} can be a password".format(pwd))
else:
    print("{} can't be a password".format(pwd))