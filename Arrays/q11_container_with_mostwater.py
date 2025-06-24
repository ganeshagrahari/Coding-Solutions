class Solution(object):
    def maxArea(self,height):
        res = 0
        l,r = 0,len(height)-1
        while(l<r):
            area = (r-l)*min(height[l],height[r])
            res = max(area,res)
            if (height[l]<height[r]):
                l+=1
            elif(height[l]>height[r]):
                r-=1
            else:
                l+=1
                #r-=1
        return res

a1 = Solution()                
print(a1.maxArea([1,8,6,2,5,4,8,3,7]))
                