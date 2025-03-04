class Solution {
    public void swap(int arr[],int i, int j){
        arr[i]=(arr[i]+arr[j])-(arr[j]=arr[i]);
    }
    public void moveZeroes(int[] nums) {
        int i =0;
        for (int j =0;j<nums.length;j++){
            if(nums[j] != 0){
                swap( nums,i,j);
                i++;
            }
        }
        
    }
}