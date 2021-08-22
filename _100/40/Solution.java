import java.util.Arrays;
import java.util.LinkedList;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList();
        Arrays.sort(candidates);
        combinatrics(candidates, 0, target, list, new LinkedList<Integer>());
        return list;
    }

    public void combinatrics(int[] candidates, int start, int target, List<List<Integer>> list,
            LinkedList<Integer> listin) {
        if (target == 0) {
            list.add(new ArrayList<Integer>(listin));
            return;
        }
        if (target < 0) {
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1])
                continue;
            listin.add(candidates[i]);
            combinatrics(candidates, i + 1, target - candidates[i], list, listin);
            listin.removeLast();
        }
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7,
                30, 12, 33, 20, 21, 29, 24, 17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33,
                10, 32, 22, 13, 34, 18, 12 };
        List<List<Integer>> res = (new Solution()).combinationSum2(candidates, 27);
        System.out.println(res);
    }
}