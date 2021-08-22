public class Solution2 {
    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[n - 1] = 0;
        for (int i = n - 2; i >= 0; i--) {
            dp[i] = Integer.MAX_VALUE - 3;
            if (nums[i] == 0) {
                continue;
            }
            int jump = nums[i];
            for (int j = i + 1; j < n && j < i + 1 + jump; j++) {
                dp[i] = Math.min(dp[i], dp[j] + 1);
            }
        }
        return dp[0];
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 2, 3, 0, 1, 4 };
        int res = (new Solution2()).jump(candidates);
        System.out.println(res);
    }
}
