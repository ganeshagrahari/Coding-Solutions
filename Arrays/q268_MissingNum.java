class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expected_sum = n*(n+1)/2;
        int actual_sum = 0;
        for(int i=0;i<n;i++){
            actual_sum+=nums[i];
        }
        return (expected_sum - actual_sum);
    }
}