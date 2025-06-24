class Solution {
    public int maximumCount(int[] nums) {
        int n  = nums.length;
        int end = n-1;
        int negativeposition = BinarySearch(nums,0,end,-1);
        int positiveposition= BinarySearch(nums,negativeposition,end,0);
        int countpositive = (n-positiveposition);
        return Math.max(negativeposition,countpositive);
        
        
    }
    public int BinarySearch(int[] nums, int start, int end , int target){
        //first >=0(>-1) position for finding negative element count 
        // fisrt > 0 position for finding count of positive element 
        
        while(start<=end){
            int mid = start + (end-start)/2;
            if(nums[mid]<=target){
                //rightsearch
                start = mid+1;
            }
            else{
                //leftsearch
                end = mid-1;
            }
        }
        return start;
    }
}    