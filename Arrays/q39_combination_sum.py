#q39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, sol = [],[]
        nums  = candidates
        n = len(nums)
        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return 
            if curr_sum > target or i ==n:
                return 
            backtrack(i+1,curr_sum)

            sol.append(nums[i])
            backtrack(i,curr_sum+nums[i])

            sol.pop()
        backtrack(0,0)
        return res            
        