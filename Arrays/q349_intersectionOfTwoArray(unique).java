import java.util.ArrayList;
import java.util.HashSet;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
       //creating a hash set :--
       HashSet<Integer> set = new HashSet<>();
       for (int n1 :nums1){
        set.add(n1);
       }
       //Array list for add frequency
       ArrayList<Integer> list = new ArrayList<>();
       for(int n2 :nums2){
        if(set.contains(n2)){
            list.add(n2);
            set.remove(n2);
        }
       }
       int k = list.size();
       int res[] = new int[k];
       for(int i=0;i<k;i++){
        res[i]=list.get(i);
       }

       return res;

       
        
    }
}