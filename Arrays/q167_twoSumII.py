# 167. Two Sum II - Input array is sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers, index1 and index2, such that index1 < index2.
# Your solution must use only constant extra space.
# You may not use the same element twice.
# You can return the answer in any order.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while (left<right):
            total = numbers[left] + numbers[right]
            if total == target :
                return [left+1,right+1]
            elif total<target:
                left+=1
            else:
                right-=1        
                
        