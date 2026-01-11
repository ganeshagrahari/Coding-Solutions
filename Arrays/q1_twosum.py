class Solution:
    def twoSum(self, nums, target):
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return None
      PrevMap = {} #val : index

      for i, num in enumerate(nums):
         diff = target - num
         if diff in PrevMap:
            return [PrevMap[diff], i]
         PrevMap[num] = i
         


s1 = Solution()
print(s1.twoSum([1,2,3,4,7],9))