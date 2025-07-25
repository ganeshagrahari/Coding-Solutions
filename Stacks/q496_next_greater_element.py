class Solution:
    def next_greate(self,nums1,nums2):
        nums1Idx = {n:i for i, n in enumerate(nums1)} #hashmap
        res = [-1]*len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur>stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur 
            if cur in nums1Idx:
                stack.append(cur)
        return res            
            
