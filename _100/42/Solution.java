public class Solution {
    public int trap(int[] height) {
        int result = 0;
        for (int i = 1; i < height.length - 1; i++) {
            int leftMax = 0;
            for (int j = 0; j < i; j++) {
                leftMax = Math.max(leftMax, height[j]);
            }

            int rightMax = 0;
            for (int k = i; k < height.length; k++) {
                rightMax = Math.max(rightMax, height[k]);
            }
            result = result + Math.max(0, Math.min(leftMax, rightMax) - height[i]);
        }
        return result;
    }

    public static void main(String arg[]) {
        int[] candidates = new int[] { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
        int res = (new Solution()).trap(candidates);
        System.out.println(res);
    }
}
