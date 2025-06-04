'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.
'''

def find_outlier(integers):
	even_nums = []
	odd_nums  = []
	for num in integers:
		if num % 2 == 0:
			even_nums.append(num)
		else:
			odd_nums.append(num)
	if len(even_nums) == 1:
		return even_nums[0]
	return odd_nums[0]
