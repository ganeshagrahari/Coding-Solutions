class solution :
    def serachrange(self,nums,target):
        def first_position(nums,target):
            l,r = 0,len(nums)-1
            index =-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]>=target:
                    r  = mid -1
                else:
                    l = mid+1

                if nums[mid] == target:
                    index = mid

            return index                
        def last_position(nums,target):
            l,r = 0,len(nums)-1
            index =-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]<=target:
                    l = mid+1
                else:
                    r = mid-1

                if nums[mid] == target:
                    index = mid

            return index  
        return [first_position(nums,target),last_position(nums,target)]              
    
