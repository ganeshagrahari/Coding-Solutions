class solution:
    def close_three_sum(self,nums,target):
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo,hi= i+1, n-1
            while lo<hi :
                cur_sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - cur_sum) < abs(target - closest_sum):
                    closest_sum = cur_sum

                if cur_sum == target:
                    return cur_sum    
                elif cur_sum<target:
                    lo+=1
                else:
                    hi-1
        return closest_sum                    