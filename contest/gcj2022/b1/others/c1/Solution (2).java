import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
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
        Intranets solver = new Intranets();
        int testCount = Integer.parseInt(in.next());
        for (int i = 1; i <= testCount; i++)
            solver.solve(i, in, out);
        out.close();
    }

    static class Intranets {
        int MOD = 1000000007;

        public void solve(int testNumber, FastScanner in, PrintWriter out) {
            long time = System.currentTimeMillis();
            out.printf("Case #%d: ", testNumber);
            solveOne(in, out);
            System.err.printf("Test #%d solved in %d ms\n", testNumber, System.currentTimeMillis() - time);
        }

        public void solveOne(FastScanner in, PrintWriter out) {
            int m = in.nextInt(), k = in.nextInt();

            out.println(fast(m, k));
//        for (int i = 2; i <= 30; i++) {
//            for (int j = 1; j <= i / 2; j++) {
//                System.err.println(i + " " + j);
//                int a1 = slow(i, j), a2 = fast(i, j);
//                if (a1 != a2) {
//                    System.err.println("!!!");
//                    System.err.print(" " + getF(slow(i, j)));
//                    System.err.print(" " + getF(fast(i, j)));
//                    System.err.println();
//                    throw new AssertionError();
//                }
//            }
//        }
        }

        int fast(int m, int k) {
            m--;
            k--;
            Combinations comb = new Combinations(m + 1, MOD);
            long num = MathUtils.modPow(2, m - 2 * k + 1, MOD) * (long) comb.choose(m - 1, 2 * k) % MOD;
            num = num * comb.choose(2 * k, k) % MOD * comb.inv[k + 1] % MOD;

            long denom = odd(2 * m) * MathUtils.inv(odd(m), MOD) % MOD * MathUtils.inv(odd(m + 1), MOD) % MOD;
            long ans = (num * MathUtils.inv(denom * 2 % MOD, MOD) % MOD);
//        if (m % 2 == 0) {
            ans = ans * MathUtils.inv(2, MOD) % MOD;
//        }
            return (int) ans;
        }

        private long odd(int n) {
            long result = 1;
            for (int i = 1; i <= n; i++) {
                int j = i;
                result = result * j % MOD;
            }
            return result;
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

    }

    static class MathUtils {
        public static int modPow(int a, long b, int mod) {
            while (a < 0) {
                a += mod;
            }
            int res = 1;
            while (b > 0) {
                if ((b & 1) != 0) {
                    res = (int) ((long) res * a % mod);
                }
                a = (int) ((long) a * a % mod);
                b >>>= 1;
            }
            return res;
        }

        public static long modPow(long a, long b, long mod) {
            while (a < 0) {
                a += mod;
            }
            long res = 1;
            while (b > 0) {
                if ((b & 1) != 0) {
                    res = res * a % mod;
                }
                a = a * a % mod;
                b >>>= 1;
            }
            return res;
        }

        public static long inv(long a, long mod) {
            return modPow(a, mod - 2, mod);
        }

        public static int[] inverses(int size, int mod) {
            int[] inv = new int[size];
            inv[1] = 1;
            for (int i = 2; i < inv.length; i++) {
                inv[i] = (int) ((long) (mod - mod / i) * inv[mod % i] % mod);
            }
            return inv;
        }

    }

    static class Combinations {
        public final int max;
        public final int mod;
        public int[] inv;
        public int[] fact;
        public int[] invFact;

        public Combinations(int max, int mod) {
            this.max = max;
            this.mod = mod;
            inv = MathUtils.inverses(max, mod);
            fact = new int[max];
            invFact = new int[max];
            fact[0] = invFact[0] = 1;
            for (int i = 1; i < max; i++) {
                fact[i] = (int) ((long) fact[i - 1] * i % mod);
                invFact[i] = (int) ((long) invFact[i - 1] * inv[i] % mod);
            }
        }

        public int choose(int n, int k) {
            if (k < 0 || k > n) {
                return 0;
            }
            return (int) ((long) fact[n] * invFact[k] % mod * invFact[n - k] % mod);
        }

    }
}

