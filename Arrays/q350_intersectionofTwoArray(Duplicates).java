import java.util.ArrayList;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int freqArr[] =new int[1001];
        // Check the frequency of num1 elements
        for(int num : nums1){
            freqArr[num]++;
        }
        ArrayList<Integer> list = new ArrayList<>();
        for(int num:nums2){
            if(freqArr[num]>0){
                list.add(num);
                freqArr[num]--;
            }
        }
        int k =list.size();
        int res[]= new int[k];
        for (int i =0;i<k;i++){
            res[i] = list.get(i);
        }
        return res;
    }
}