
class CodesCracker:
    def HexToOct(self, h):
        return oct(int(h, 16))

print("Enter Hexadecimal Number: ", end="")
hnum = input()

obj = CodesCracker()
onum = obj.HexToOct(hnum)
print("\nEquivalent Octal Value = ", onum[2:])