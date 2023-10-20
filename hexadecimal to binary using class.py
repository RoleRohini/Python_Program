
class CodesCracker:
    def HexToBin(self, h):
        return bin(int(h, 16))

print("Enter the Hexadecimal Number: ", end="")
hnum = input()

obj = CodesCracker()
bnum = obj.HexToBin(hnum)
print("\nEquivalent Binary Value = ", bnum[2:])