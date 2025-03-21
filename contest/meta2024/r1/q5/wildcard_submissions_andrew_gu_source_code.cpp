#pragma GCC optimize("O2")
#include <iostream>
using namespace std;

const bool FILEMODE = 1;
const int L = 100;
const int MOD = 998244353;
const int K = 26;
using bs = bitset<L>;

string merge(string s, string t) {
  string res;
  for (size_t i = 0; i < min(s.size(), t.size()); i++) {
    if (s[i] == '?') res.push_back(t[i]);
    else if (t[i] == '?') res.push_back(s[i]);
    else if (s[i] == t[i]) res.push_back(s[i]);
    else break;
  }
  return res;
}

int get_len(string& s, string& t) {
  int m = min(s.size(), t.size());
  for (int i = 0; i < m; i++) {
    if (s[i] != '?' && t[i] != '?' && s[i] != t[i]) return i;
  }
  return m;
}

void add(int& x, int y) {
  x += y;
  if (x >= MOD) x -= MOD;
}

void sub(int& x, int y) {
  x -= y;
  if (x < 0) x += MOD;
}

int main () {
  ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int n;
    cin >> n;
    vector<string> s(n);
    for (auto& x: s) cin >> x;
    vector<bs> fixed(1<<n);
    vector<vector<int>> len_calc(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        len_calc[i][j] = get_len(s[i], s[j]);
      }
    }
    vector<int> len(1<<n), tmp(1<<n);
    len[0] = L;
    for (int i = 0; i < n; i++) {
      bs cur;
      for (int j = 0; j < (int)s[i].size(); j++) { 
        if (s[i][j] != '?') cur.set(j);
      }
      tmp[0] = L+1;
      for (int j = 0; j < i; j++) {
        for (int k = 0; k < (1<<j); k++) {
          tmp[k|(1<<j)] = min(tmp[k], len_calc[i][j]);
        }
      }
      for (int j = 0; j < (1<<i); j++) {
        if (j == 0) len[j|(1<<i)] = (int)s[i].size();
        else len[j|(1<<i)] = min(len[j], tmp[j]);
        fixed[j|(1<<i)] = fixed[j] | cur;
      }
    }

    int ans = 0;
    for (int mask = 1; mask < (1<<n); mask++) {
      int wt = 1;
      for (int i = 0; i < len[mask]; i++) {
        if (!fixed[mask][i]) wt = 1LL * wt * K % MOD;
        if (__builtin_popcount(mask) % 2 == 1) add(ans, wt);
        else sub(ans, wt);
      }
    }
    add(ans, 1); // empty string
    cout << "Case #" << tc << ": " << ans << '\n';
  }
}
