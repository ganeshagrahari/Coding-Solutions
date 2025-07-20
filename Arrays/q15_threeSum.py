# leetcode 15. 3Sum
# https://leetcode.com/problems/3sum/
# Time: O(n^2)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,n-1
            while l<r :
                sum = nums[i]+nums[l]+nums[r]
                if sum ==0 :
                    ans.append([nums[i],nums[l],nums[r]])
                    l,r=l+1,r-1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif sum < 0:
                    l+=1
                else:
                    r-=1
        return ans                       
