class solution:
    def product(self,nums):
        n = len(nums)
        l_mult,r_mult = 1,1
        l_arr,r_arr = [0]*n,[0]*n
        for i in range(n):
            j = -i-1
            l_arr[i] = l_mult
            r_arr[j] = r_mult

            l_mult*=nums[i]
            r_mult*nums[j]

        return  (l*r for l, r in zip(l_arr,r_arr))    