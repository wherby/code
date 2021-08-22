import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        HashMap<Integer, Boolean> mp = new HashMap<Integer, Boolean>();
        Integer[] interim = new Integer[nums.length];
        List<List<Integer>> output = new ArrayList<>();
        permuteCur(nums, 0, interim, output, mp);
        return output;
    }

    public void permuteCur(int[] nums, int index, Integer[] interim, List<List<Integer>> lists,
            HashMap<Integer, Boolean> mp) {
        if (index == nums.length) {
            int res = 0;
            for (int i = 0; i < interim.length; i++) {
                res = res * 10 + interim[i];
            }
            if (mp.getOrDefault(res, false) == false) {
                lists.add(Arrays.asList(interim));
                mp.put(res, true);
            }
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (interim[i] == null) {
                Integer[] arr = Arrays.copyOf(interim, interim.length);
                arr[i] = nums[index];
                permuteCur(nums, index + 1, arr, lists, mp);
                // System.out.println(Arrays.asList(arr));
            }
        }
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 1, 2, 1 };
        List<List<Integer>> res = (new Solution()).permuteUnique(candidates);
        System.out.println(res);
    }
}
