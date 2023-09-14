
num=int(input("enter a number"))#num=15
check=0
for i in range (2,num):
    if num%i==0:
        check=1
        break
if check == 1:
    print("not prime")
else:
    print("prime")