public class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[n - 1] = 0;
        for (int i = n - 2; i >= 0; i--) {
            dp[i] = Integer.MAX_VALUE;
            if (nums[i] == 0) {
                continue;
            }
            int jump = nums[i];
            for (int j = i + 1; j < n && j < i + 1 + jump; j++) {
                dp[i] = Math.min(dp[i], dp[j] == Integer.MAX_VALUE ? dp[j] : dp[j] + 1);
            }
        }
        return dp[0];
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 2, 3, 1, 1, 4 };
        int res = (new Solution()).jump(candidates);
        System.out.println(res);
    }
}
