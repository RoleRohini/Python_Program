
# Python 3 code to find sum
def _sum(arr):
	sum = 0
	for i in arr:
		sum = sum + i

	return(sum)

if __name__ == "__main__":
	arr = [2, 3, 4, 1]
	n = len(arr)
	ans = _sum(arr)
	print('Sum of the array is ', ans)


