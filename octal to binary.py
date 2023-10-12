
print("Enter the Octal Number: ")
octnum = int(input())

rev = 0
chk = 0

while octnum!=0:
    rem = octnum%10
    if rem>7:
        chk = 1
        break
    rev = rem + (rev*10)
    octnum = int(octnum/10)

if chk == 0:
    octnum = rev
    binnum = ""

    while octnum!=0:
        rem = octnum%10
        if rem==0:
            binnum = binnum + "000"
        elif rem==1:
            binnum = binnum + "001"
        elif rem==2:
            binnum = binnum + "010"
        elif rem==3:
            binnum = binnum + "011"
        elif rem==4:
            binnum = binnum + "100"
        elif rem==5:
            binnum = binnum + "101"
        elif rem==6:
            binnum = binnum + "110"
        elif rem==7:
            binnum = binnum + "111"
        octnum = int(octnum/10)

    print("\nEquivalent Binary Value = ", binnum)

else:
    print("\nInvalid Input!")