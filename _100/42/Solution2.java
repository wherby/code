public class Solution2 {
    public int trap(int[] height) {
        int n = height.length;
        if (n == 0) {
            return 0;
        }

        int[] leftMax = new int[n];
        int[] rightMax = new int[n];
        leftMax[0] = height[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], height[i]);
        }
        rightMax[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], height[i]);
        }

        int result = 0;
        for (int i = 1; i < n - 1; i++) {
            result = result + Math.max(0, Math.min(leftMax[i], rightMax[i]) - height[i]);
        }
        return result;
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
        int res = (new Solution()).trap(candidates);
        System.out.println(res);
    }
}
