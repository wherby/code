import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.util.stream.IntStream;
import java.util.Arrays;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.FileNotFoundException;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Solution {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastScanner in = new FastScanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Squary solver = new Squary();
        int testCount = Integer.parseInt(in.next());
        for (int i = 1; i <= testCount; i++)
            solver.solve(i, in, out);
        out.close();
    }

    static class Squary {
        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            long time = System.currentTimeMillis();
            out.printf("Case #%d: ", testNumber);
            solveOne(in, out);
            System.err.printf("Test #%d solved in %d ms\n", testNumber, System.currentTimeMillis() - time);
        }

        public void solveOne(FastScanner in, PrintWriter out) {
            int n = in.nextInt(), k = in.nextInt();
            int[] e = in.nextIntArray(n);
            if (k == 1) {
                out.println(solve1(n, e));
            } else {
                int add = -Arrays.stream(e).sum() + 1;
                int[] newE = Arrays.copyOf(e, n + 1);
                newE[n] = add;
                out.println(add + " " + solve1(n, newE));
            }
        }

        private String solve1(int n, int[] e) {
            long sum = 0, sum2 = 0;
            for (int x : e) {
                sum += x;
                sum2 += (long) x * x;
            }
            if (sum == 0) {
                if (sum2 != sum * sum) {
                    return "IMPOSSIBLE";
                } else {
                    return "0";
                }
            }
            if ((sum2 - sum * sum) % (2 * sum) != 0) {
                return "IMPOSSIBLE";
            } else {
                return Long.toString((sum2 - sum * sum) / (2 * sum));
            }
        }

    }

    static class FastScanner {
        public BufferedReader br;
        public StringTokenizer st;

        public FastScanner(InputStream in) {
            br = new BufferedReader(new InputStreamReader(in));
        }

        public FastScanner(String fileName) {
            try {
                br = new BufferedReader(new FileReader(fileName));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public String next() {
            while (st == null || !st.hasMoreElements()) {
                String line = null;
                try {
                    line = br.readLine();
                } catch (IOException e) {
                    throw new UnknownError();
                }
                if (line == null) {
                    throw new UnknownError();
                }
                st = new StringTokenizer(line);
            }
            return st.nextToken();
        }

        public int[] nextIntArray(int n) {
            int[] ret = new int[n];
            for (int i = 0; i < n; i++) {
                ret[i] = nextInt();
            }
            return ret;
        }

    }
}

