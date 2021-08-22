import java.util.ArrayList;
import java.util.List;

class Solution {
    static int[][] board;
  static int count =0;
  static List<List<String>> result;

  public int totalNQueens(int n) {
      count =0; // The static variable will not clean in test cases
      board = new int[n][n];
      result = new ArrayList<>();
      solveNQueenProblem(0, n);
      return count;
  }

  public List<List<String>> solveNQueens(int n) {
      board = new int[n][n];
      result = new ArrayList<>();
      solveNQueenProblem(0, n);
      System.out.println(result);
      return result;
  }

  static void prepareList(int[][] board) {
      List<String> subList = new ArrayList<>();
      for (int[] row : board) {
          StringBuilder sb = new StringBuilder();
          for (int val : row) {
              if (val == 0) {
                  sb.append(".");
              } else {
                  sb.append("Q");
              }
          }
          subList.add(sb.toString());
      }
      count = count +1;
      result.add(subList);
  }

  static private boolean isSafe(int row, int col, int n) {
      for (int i = 0; i < col; i++) {
          if (board[row][i] == 1) {
              return false;
          }
      }
      for (int i = row, j = col; i < n && j >= 0; i++, j--) {
          if (board[i][j] == 1) {
              return false;
          }
      }
      for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
          if (board[i][j] == 1) {
              return false;
          }
      }
      return true;
  }

  private static void solveNQueenProblem(int col, int n) {
      if (col == n) {
          prepareList(board);
      }
      for (int i = 0; i < n; i++) {
          if (isSafe(i, col, n)) {
              board[i][col] = 1;
              solveNQueenProblem(col + 1, n);
              board[i][col] = 0;
          }
      }
  }


  public static void main(String arg[]) {
    int res = (new Solution()).totalNQueens(1);
    System.out.println(res);
}
}