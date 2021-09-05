import java.util.*;
class Solution {

  private static final String alphabet = "abcd";
  private static final int mod = 1_000_000_007;
  private Map<Integer, Integer> dp ;
  private int[][] prev;
  private int[][] next;

  public int countPalindromicSubsequences(String S) {
    dp = new HashMap<>(S.length());
    prev = new int[S.length()][alphabet.length()];
    next = new int[S.length()][alphabet.length()];

    final int[] nextIndexes = new int[alphabet.length()];
    Arrays.fill(nextIndexes, -1);
    for (int i = 0; i < S.length(); i++) {
      nextIndexes[S.charAt(i) - 'a'] = i;
      prev[i] = nextIndexes.clone();
    }
    Arrays.fill(nextIndexes, -1);
    for (int i = S.length() - 1; i >=0 ; i--) {
      nextIndexes[S.charAt(i) - 'a'] = i;
      next[i] = nextIndexes.clone();
    }

    return countPalindromicSubsequences(S, 0, S.length() - 1) - 1;
  }

  private int countPalindromicSubsequences(String S, int start, int end) {
    return dp.computeIfAbsent(start * S.length() + end, coord ->
        (start > end) ? 1 : IntStream.range(0, alphabet.length()).reduce(1, (sum, c) -> {
          final int nextStart = next[start][c];
          final int nextEnd = prev[end][c];
          if (start <= nextStart && nextStart <= end) {
            sum++;
          }
          if (nextStart != -1 && nextStart < nextEnd) {
            sum += countPalindromicSubsequences(S, nextStart + 1, nextEnd - 1);
            sum %= mod;
          }
          return sum;
        }) % mod
    );
  }

  public static void main(String args[]) { 
        System.out.println("Hello World!"); 
    } 

}