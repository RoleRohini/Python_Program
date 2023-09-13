#palindrome
str1=input("enter string : ")
b=str1[::-1]
if str1==b:
    print("palindrome")
else:
    print("not palindrome")