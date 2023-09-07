
username=input("Enter your name:")
password=input("enter your password :")
password_length=len(password)
hidden_password=password_length * '*'
print (username,"your password", hidden_password,"is",password_length ,'letters long')