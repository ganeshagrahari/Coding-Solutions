

public class q108_ArrayToBst {
    int val;
    q108_ArrayToBst left;
    q108_ArrayToBst right;
    q108_ArrayToBst() {}
    q108_ArrayToBst(int val) { this.val = val; }
    q108_ArrayToBst(int val, q108_ArrayToBst left, q108_ArrayToBst right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
 
class Solution {
    public q108_ArrayToBst sortedArrayToBST(int[] nums) {
        if(nums.length==0){
            return null;
        }
        return getbst(nums,0,nums.length-1);
    }
    public q108_ArrayToBst getbst(int nums [], int startIdx,int endIdx){
        if(startIdx>endIdx){
            return null;
        }
        int midleIdx = (startIdx+endIdx)/2;
        q108_ArrayToBst bst = new q108_ArrayToBst(nums[midleIdx]);

        bst.left =getbst(nums,startIdx,midleIdx-1 );
        bst.right=getbst(nums,midleIdx+1,endIdx);
        return bst;
    }
}