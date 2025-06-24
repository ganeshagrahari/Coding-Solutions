from collections import defaultdict
# 4Sum II

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """

        ans =0
        sum_map=defaultdict(int)
        for a in nums1:
            for b in nums2:
                sum_map[a+b]+=1

        for c in nums3:
            for d in nums4:
                    ans+=sum_map.get(-(c+d),0)

        return ans            
        