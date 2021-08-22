import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList<>();
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
            listin.add(candidates[i]);
            combinatrics(candidates, i, target - candidates[i], list, listin);
            listin.removeLast();
        }
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 2, 3, 6, 7 };
        List<List<Integer>> res = (new Solution()).combinationSum(candidates, 7);
        System.out.println(res);
    }
}