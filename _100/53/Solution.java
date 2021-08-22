public class Solution {
    public int maxSubArray(int[] nums) {
        int MINV = -1000000;
        int tmp =0;   
        for(int i = 0; i< nums.length;i++){
            if(tmp <0){
                tmp =0;
            }
            tmp = tmp + nums[i];
            if(tmp > MINV){
                MINV = tmp;
            }
        }
        return MINV;
    }
}
