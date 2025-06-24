#LeetCode question 384
# Shuffle an Array
#https://leetcode.com/problems/shuffle-an-array/
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.org=self.nums[:] # if we need to do reset we can directly return this original array
        

    def reset(self):
        """
        :rtype: List[int]
        """
        self.nums=self.org[:]
        return self.nums
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        random.shuffle(self.nums)
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()