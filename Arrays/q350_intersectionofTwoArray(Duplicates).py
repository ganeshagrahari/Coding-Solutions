'''import java.util.ArrayList;

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
}'''

#apporch:-
'''🧠 Idea of the Solution (frequency array approach):
We’ll use a counting method:

First, count how many times each number appears in nums1.

Then, check nums2 one by one:

->If a number is in nums1 and still available (not all used), we add it to the result.

->Decrease its count (since we used it once).'''

class Solution:
    def intersect(self,nums1,nums2):
        freqArr= [0]*1001
        # Here we will each count of each element in this freqArr
        for num in nums1:
            freqArr[num]+=1
        
        #creating a empty list 
        result =[]
        
        # we  will check each element one by one 
        for num in nums2:
            if(freqArr[num]>0):
                result.append(num)    
                freqArr[num]-=1
        return result        

s1= Solution()
print(s1.intersect([1,2,4,8,7],[2,8,6,5]))