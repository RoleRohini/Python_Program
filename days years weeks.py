
print("Enter the Number of Days: ")
num = int(input())

year = int(num/365)
week = int((num%365)/7)
days = int((num%365)%7)

print("Total Number of Year(s): ")
print(year)
print("Total Number of Week(s):")
print(week)
print("Total Number of Day(s):")
print(days)