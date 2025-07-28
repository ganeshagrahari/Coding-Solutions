class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            unique_set = set()
            for i in range(start,len(nums)):
                if nums[i] in unique_set :
                    continue

                unique_set.add(nums[i])
                nums[start] ,nums[i] = nums[i], nums[start] 
                backtrack(start +1)
                nums[start] ,nums[i] = nums[i], nums[start]  

        backtrack(0)
        return result           
