
list_1 = [1, 2, 1, 4, 6,12,14,2,3,45,988]

print(list(set(list_1)))

# another method
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))