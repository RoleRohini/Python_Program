
num=int(input("enter a number : "))
rev=0
while num > 0:
    a=num%10
    rev=rev*10+a
    num=num//10

print(rev)

#another method
num = 12345
print(str(num)[::-1])