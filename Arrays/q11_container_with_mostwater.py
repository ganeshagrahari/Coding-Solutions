class Solution(object):
    def maxArea(self, height):
        l,r = 0, len(height)-1
        res = 0
        while (l<r):
            area = (r-l)*min(height[l],height[r])
            res = max(area,res)
            if(height[l]>height[r]):
                r-=1
            elif(height[r]>height[l]):
                l+=1
            else :
                l+=1        
        return res         


a1 = Solution()                
print(a1.maxArea([1,8,6,2,5,4,8,3,7]))
                