import java.util.Arrays;

class Solution {
    public void rotate(int[][] matrix) {
        int len2 = matrix.length / 2, len1 = len2, len = matrix.length;
        len2 += matrix.length % 2 == 0 ? 0 : 1;

        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                exchangeEle(matrix, j, len - 1 - i, i, j);
                exchangeEle(matrix, len - 1 - i, len - 1 - j, i, j);
                exchangeEle(matrix, len - 1 - j, i, i, j);
            }
        }
    }

    public void exchangeEle(int[][] matrix, int x1, int y1, int x2, int y2) {
        int temp = matrix[x1][y1];
        matrix[x1][y1] = matrix[x2][y2];
        matrix[x2][y2] = temp;
    }

    public static void main(String arg[]) {
        int[][] matrix = new int[][] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
        (new Solution()).rotate(matrix);
        System.out.println(Arrays.deepToString(matrix));
    }
}