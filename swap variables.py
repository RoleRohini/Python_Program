
print("Enter any Value for First Variable: ", end="")
variableOne = input()
print("Enter any Value for Second Variable: ", end="")
variableTwo = input()

print("\nBefore Swap:")
print("Value of \"variableOne\" =", variableOne)
print("Value of \"variableTwo\" =", variableTwo)

x = variableOne
variableOne = variableTwo
variableTwo = x

print("\nAfter Swap:")
print("Value of \"variableOne\" =", variableOne)
print("Value of \"variableTwo\" =", variableTwo)
