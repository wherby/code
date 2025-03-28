#pragma GCC optimize("Ofast","unroll-all-loops","fast-math","no-stack-protector")
#include<iostream>
using namespace std;
#define fi first
#define se second
#if 1
void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}
template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '['; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "]";}
void _print() {cerr << endl << flush;}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#define DEBUG(x...) cerr << "*["<<__LINE__<<"]\t"<< #x << " = "; _print(x)
template<class T>
istream& operator>>(istream& is, vector<T>& v) {
	int n; is>>n; v.resize(n);
	for(auto &i:v) is>>i;
	return is;
}
template<class T1,class T2>
istream& operator>>(istream& is, pair<T1,T2>& p) {
	is>>p.fi>>p.se;
	return is;
}
template<class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
	for(const auto &i:v) os<<i<<' ';
	return os;
}
template<class T1,class T2>
ostream& operator<<(ostream& os, const pair<T1,T2>& p) {
	os<<p.fi<<' '<<p.se; return os;
}
#endif
 
#define ll long long
#define mp make_pair
#define pb push_back
#define vi vector<ll>
#define pi pair<int, int>
#define mod 998244353
template<typename T> bool chkmin(T &a, T b){return (b < a) ? a = b, 1 : 0;}
template<typename T> bool chkmax(T &a, T b){return (b > a) ? a = b, 1 : 0;}
ll ksm(ll a, ll b) {if (b == 0) return 1; ll ns = ksm(a, b >> 1); ns = ns * ns % mod; if (b & 1) ns = ns * a % mod; return ns;}

const int maxn = 1e5 + 5;
char s[maxn];

int dp[maxn][10];
bool mat[maxn];

char t[maxn];
int ways[maxn];
int opt[maxn];

bool good(int u, int v) {
	if (u == 0) return 0;
	if (u >= 3) return 0;
	if (u == 1) return 1;
	if (u == 2 && v <= 6) return 1;
	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
		scanf("%s", s + 1);
		int l = strlen(s + 1);
		for (int i = 1; i <= l; i++) {
			t[i] = s[i];
			if (s[i] == '?') t[i] = '1';
		}
		ways[l + 1] = 1;
		for (int i = l; i >= 1; i--) {
			ways[i] = 0;
			if (t[i] > '0') ways[i] = ways[i + 1];
			if (i + 1 <= l && good(t[i] - '0', t[i + 1] - '0')) {
				ways[i] += ways[i + 2];
				ways[i] %= mod;
			}
		}

		int k;
		cin >> k;
		for (int i = 1; i <= l; i++) {
			mat[i] = 0;
			if (s[i] == '0') mat[i - 1] = 1;
		}
		for (int i = l; i >= 1; i--) {
			for (int c = 0; c < 10; c++) {
				if (i == l) dp[i][c] = 1;
				else {
					dp[i][c] = 0;
					for (int nx = 0; nx < 10; nx++) {
						if (mat[i + 1]) dp[i][c] += dp[i + 1][nx];
						else {
							if (!good(c, nx) && good(t[i] - '0', t[i + 1] - '0'))
								continue;
							dp[i][c] += dp[i + 1][nx];
						}
					}
					dp[i][c] = min(dp[i][c], k + 1);
 				}
				if (s[i] != '?' && s[i] - '0' != c) dp[i][c] = 0;
				if (s[i] == '?' && c == 0) dp[i][c] = 0;
			}
		}
		for (int i = 1; i <= l; i++) {
			for (int c = 9; c >= 0; c--) {
				if (!mat[i]) {
					if (i > 1 && !good(s[i - 1] - '0', c) && good(t[i - 1] - '0', t[i] - '0'))
						continue;
				}
				if (dp[i][c] < k) k -= dp[i][c];
				else {
					s[i] = '0' + c;
					break;
				}
			}
		}
		printf("Case #%d: %s %d\n", i, s + 1, ways[1]);
	}
    return 0;
}