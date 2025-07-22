class Solution :
    def search(self,nums,target):
        n = len(nums)
        low,high = 0,n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] ==  target:
                return mid
            elif nums[mid]<target:
                low = mid +1
            else:
                high = mid -1    

a1 = Solution()
print(a1.search([1,3,5,7,9,11],0))
