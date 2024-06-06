#1. Write a python program, to accept a list of integers and print the sum of all 5 divisible numbers using recursion.
 
# Child function to parent function
def findSum(index, nums, n):
	if index == n:
		return 0 
	nextEleSum = findSum(index + 1, nums, n)
	if nums[index] % 5 == 0:
		nextEleSum += nums[index] 
	return nextEleSum
 
# parent function to child function 
def findSum2(index, nums, n, result):
	if index == n:
		print("Sum is:", result)
		return 
	if nums[index] % 5 == 0:
		result += nums[index]
	findSum2(index + 1, nums, n, result)
	
#2. write a python program to print all even indexed elements in both left to right and right to left manner using recursion.
 
def printLeftToRight(index, nums, n):
	if index == n:
		return 
 
	if index % 2 == 0:
		print(nums[index])
	printLeftToRight(index + 1, nums, n)
 
def printLeftToRightBetterOne(index, nums, n):
	if index >= n:
		return 
 
	print(nums[index])
	printLeftToRightBetterOne(index + 2, nums, n)
 
def printRightToLeftBetterOne(index, nums, n):
	if index >= n:
		return 
 
	printLeftToRightBetterOne(index + 2, nums, n)
	print(nums[index])
	
nums=[10,20,45,67]
printLeftToRight(0, nums, len(nums))

 
 
 
def printRightToLeftInReverseManner(index, nums, n):
	if index < 0:
		return 
	print(nums[index])
	printRightToLeftInReverseManner(index - 2, nums, n)
 
 
nums=list(map(int,input().split()))
n = len(nums)
if n % 2 == 0:
    printRightToLeftInReverseManner(n - 2, nums, n)
else:
    printRightToLeftInReverseManner(n - 1, nums, n)

