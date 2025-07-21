class solution : 
    def rotate(self,nums,k):
        n = len(nums)
        k = k%n # hadle k>n

        def reverse(start,end):
            while start<end :
                nums[start],nums[end] = nums[end],nums[start]
                start +=1
                end -=1

        #for right rotation         
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        #for left rotation
        reverse(0,k-1)
        reverse(k,n-1)
        reverse(0,n-1)
