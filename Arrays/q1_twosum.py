'''class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            for (int j=i+1; j<nums.length;j++){
                if(nums[i]+nums[j]==target){
                    int a[]={i,j};
                    return a ;
                }
            }
        }
        return null;
        
    }
}'''
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

s1 = Solution()
print(s1.twoSum([2,1,3,5,4,2,3],5))