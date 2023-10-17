
print("Enter the Octal Number: ")
octnum = int(input())

chk = 0
i = 0
decnum = 0
while octnum!=0:
    rem = octnum%10
    if rem>7:
        chk = 1
        break
    decnum = decnum + (rem * (8 ** i))
    i = i+1
    octnum = int(octnum/10)

if chk == 0:
    print("\nEquivalent Decimal Value =", decnum)
else:
    print("\nInvalid Input!")