
nums = []
print("Enter the Size of List: ")
tot = int(input())

print("Enter " + str(tot) + " Numbers: ")
for i in range(tot):
    nums.insert(i, int(input()))

for i in range(tot-1):
    for j in range(tot-i-1):
        if nums[j]>nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

print("The Sorted List is:")
for i in range(tot):
    print(nums[i])