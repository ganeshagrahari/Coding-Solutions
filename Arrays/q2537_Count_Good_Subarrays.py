from collections import defaultdict
class  Object:
    def count_good_subarray(self,nums,k):
        freq = defaultdict(int) # to count frequency of number
        n = len(nums) #length of array
        i = 0 #left pointer
        j=0#right pointer
        pairs= 0 #count of pairs
        result = 0 #count of valid subarrays
        
        while j<n:
            pairs+=freq[nums[j]]# means  jitne bar j aay hai phle utne pair banege
            freq[nums[j]]+=1 # adding frequency of j 
            while(pairs>=k): # giving condition for valid subarray
                result+=(n-j) # means if j point pe we got our vaild subaaray to uske bad ka bhi sb valid hoga
                freq[nums[i]]-=1 # reducing frequency of nums[i]
                pairs-=freq[nums[i]] # pair se bhi hta rhe 
                i+=1 # moving i to the right
            j+=1   # moving j to right
        return result    
             
O1 = Object()             
print(O1.count_good_subarray([1,1,1,1,1],10))