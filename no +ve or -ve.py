
#Write a program which accept number from user and check whether that number is positive or negative or zero.
#---------------------------------------------------------------------------------------------------------

def ChkNum(No):

    if No>0:
        print("Positive Number")

    elif No<0:
        print("Negative Number")

    elif No==0:
        print("Number is zero")
No=int(input("Enter number"))
ChkNum(No)