import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        Integer[] interim = new Integer[nums.length];
        List<List<Integer>> output = new ArrayList<>();
        permuteCur(nums, 0, interim, output);
        return output;
    }

    public void permuteCur(int[] nums, int index, Integer[] interim, List<List<Integer>> lists) {
        System.out.println(Arrays.asList(interim));
        if (index == nums.length) {
            lists.add(Arrays.asList(interim));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (interim[i] == null) {
                Integer[] arr = Arrays.copyOf(interim, interim.length);
                arr[i] = nums[index];
                permuteCur(nums, index + 1, arr, lists);
                // System.out.println(Arrays.asList(arr));
            }
        }
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 1, 2, 3 };
        List<List<Integer>> res = (new Solution()).permute(candidates);
        System.out.println(res);
    }
}
