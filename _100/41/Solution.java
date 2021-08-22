import java.util.Arrays;

public class Solution {
    public int firstMissingPositive(int[] nums) {
        int[] arr = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i];
            if (v > 0 && v <= nums.length) {
                arr[v] = 1;
            }
        }
        for (int i = 1; i < nums.length + 1; i++) {
            if (arr[i] == 0) {
                return i;
            }
        }
        return nums.length + 1;
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 3, 4, -1, 1 };
        int res = (new Solution()).firstMissingPositive(candidates);
        System.out.println(res);
    }
}
