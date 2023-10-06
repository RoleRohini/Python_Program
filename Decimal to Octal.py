print("Enter the Decimal Number: ")
decnum = int(input())

i = 0
octnum = []
while decnum!=0:
    rem = decnum%8
    octnum.insert(i, rem)
    i = i+1
    decnum = int(decnum/8)

print("\nEquivalent Octal Value is: ")
i = i-1
while i>=0:
    print(octnum[i], end="")
    i = i-1
print()