/*169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space? */
class Solution {
    public int majorityElement(int[] nums) {
        
        int cand = 0;
        int count = 0;
        for(int i =0;i<nums.length;i++){
            //new ele if the count of the previous ele is 0
            if(count == 0){
                cand =nums[i];
            }
            //if same than increase the count
            if (cand ==nums[i]){
                count ++;
            }
            //if not same than decrease the count
            else{
                count --;
            }

        }
        return cand ;
    }
}