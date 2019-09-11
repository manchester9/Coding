# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:39:18 2019
"""

#########################
## List 2 ###############
#########################
"S8.1"
#Return the number of even ints in the given array. Note: the % "mod" operator computes the 
#remainder, e.g. 5 % 2 is 1.
#count_evens([2, 1, 2, 3, 4]) → 3
#count_evens([2, 2, 0]) → 3
#count_evens([1, 3, 5]) → 0


"S8.2"
#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 
#13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
#sum13([1, 2, 2, 1]) → 6
#sum13([1, 1]) → 2
#sum13([1, 2, 2, 1, 13]) → 6
#while i < len(nums):
def sum13(nums):
    i = 0
    tot = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            i += 1
        else: 
            tot += nums[i]
        i += 1
    return tot

sum13([1, 2, 2, 1, 13, 100, 1, 3])

"S8.3"
#Given an array length 1 or more of ints, return the difference between the largest and smallest values 
#in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger 
#of two values.
#big_diff([10, 3, 5, 6]) → 7
#big_diff([7, 2, 10, 9]) → 8
#big_diff([2, 10, 7, 2]) → 8

def big_diff(nums):
    min_num = min(nums)
    max_num = max(nums)
    diff = max_num - min_num
    return diff

big_diff([2, 10, 7, 2])

"S8.4"
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
#extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
#sum67([1, 2, 2]) → 5
#sum67([1, 2, 2, 6, 99, 99, 7]) → 5
#sum67([1, 1, 6, 7, 2]) → 4
def sum67(nums):
	tot = 0
	found = False
	for i in range(len(nums)):
		if nums[i] == 6:
			found = True
		if not found:
			tot += nums[i]
		if nums[i] == 7 and found:
			found = False
	return tot

sum67([1, 1, 6, 7, 2])


"S8.5"
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
#except ignoring the largest and smallest values in the array. If there are multiple copies of 
#the smallest value, ignore just one copy, and likewise for the largest value. Use int division to 
#produce the final average. You may assume that the array is length 3 or more.
#centered_average([1, 2, 3, 4, 100]) → 3
#centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
#centered_average([-10, -4, -2, -4, -2, 0]) → -3





"S8.6"
#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
#has22([1, 2, 2]) → True
#has22([1, 2, 1, 2]) → False
#has22([2, 1, 2]) → False


























