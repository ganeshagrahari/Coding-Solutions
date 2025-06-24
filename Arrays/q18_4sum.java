import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        int n=nums.length;
        List<List<Integer>> result = new ArrayList<>();
        for(int i=0;i<n;i++){
            if(i>0 && nums[i]==nums[i-1]) continue;
            for (int j=i+1;j<n;j++){
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                long target2 =(long)target-(long)nums[i]-nums[j];
                int left=j+1;
                int right=n-1;
                while(left<right){
                   int sum = nums[left]+nums[right];
                    if(sum<target2){
                        left++;
                    }
                    else if(sum>target2){
                        right--;
                    }
                    else {
                         // Store the quadruplet in result
                         List<Integer> list = Arrays.asList(nums[i],nums[j],nums[left],nums[right]);
                         result.add(list);
                         while(left<right && nums[left]==list.get(2)){
                            left++;
                         }
                          while(left<right && nums[right]==list.get(3)){
                            right--;
                         }
                       

                        }
                        
                }
                while(j+1<n && nums[j]==nums[j+1]){
                    j++;
                }
            }
            while(i+1<n && nums[i]==nums[i+1]){
                i++;
            }
          
        }
        return result;

        
    }
}