class Solution:
    def threeSum(self,nums):
        res = []
        nums.sort()
        n = len(nums)-1
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,n
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r :
                        l+= 1
        return res
    
s1 = Solution()
print(s1.threeSum([-1,0,1,2,-1,-4]))                            