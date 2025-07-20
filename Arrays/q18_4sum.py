# leetcode question 18. 4Sum
# https://leetcode.com/problems/4sum/
# Time: O(n^3)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        answer = []
        for i in range(n):
            if i > 0 and nums[i]==nums[i-1]:
                continue

            for j in range(i+1,n):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                

                lo, hi = j+1,n-1
                while lo<hi:
                    sum = nums[i]+nums[j]+nums[lo]+nums[hi]
                    if sum ==target :
                        answer.append([nums[i],nums[j],nums[lo],nums[hi]])
                        lo+=1
                        hi-=1
                        while lo<hi and nums[lo]==nums[lo-1]:
                            lo+=1
                        while lo<hi and nums[hi]==nums[hi+1]:
                            hi-=1
                    elif sum < target :
                        lo+=1
                    else:
                        hi-=1
        return answer                               

        