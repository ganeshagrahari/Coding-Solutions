class Solution:
    def permutation(self,nums):
        n = len(nums)
        ans, sol = [], []
        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans          
    
s1 = Solution()
print(s1.permutation([1,2,3,4,5]))    