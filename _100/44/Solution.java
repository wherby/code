public class Solution {
    public boolean isMatch(String s, String p) {
        if (s.length() > 0 && p.length() == 0) {
            return false;
        }
        int m = p.length(), n = s.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int i = 0; i < m; i++) {
            if (p.charAt(i) != '*') {
                break;
            } else {
                dp[i + 1][0] = true;
            }
        }
        for (int i = 1; i <= m; i++) {
            char c = p.charAt(i - 1);
            for (int j = 1; j <= n; j++) {
                if (c == '*') {
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
                } else if (s.charAt(j - 1) == c || c == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }
        return dp[m][n];
    }

    public static void main(String arg[]) {
        String s = "aa";
        String p = "*";
        boolean res = (new Solution()).isMatch(s, p);
        System.out.println(res);
    }

}
