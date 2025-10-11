#pragma GCC optimize("Ofast","unroll-all-loops","fast-math","no-stack-protector")
#include <bits/stdc++.h>
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
#define db double
#define mod 998244353
template<typename T> bool chkmin(T &a, T b){return (b < a) ? a = b, 1 : 0;}
template<typename T> bool chkmax(T &a, T b){return (b > a) ? a = b, 1 : 0;}
ll ksm(ll a, ll b) {if (b == 0) return 1; ll ns = ksm(a, b >> 1); ns = ns * ns % mod; if (b & 1) ns = ns * a % mod; return ns;}

const int maxn = 2505;
char s[maxn][maxn];
int x[maxn][2];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int N, K;
		cin >> N >> K;
		int b[2][2];
		b[0][0] = N, b[0][1] = 0;
		b[1][0] = N, b[1][1] = 0;
		vector<pi> pts, bds;
		int most[2][2]; 
		most[0][0] = N, most[0][1] = 0;
		most[1][0] = N, most[1][1] = 0;
		for (int j = 1; j <= N; j++) {
			x[j][0] = N + 1, x[j][1] = 0;
			scanf("%s", s[j] + 1);
			for (int k = 1; k <= N; k++) {
				if (s[j][k] == '1') {
					chkmin(b[0][0], j);
					chkmax(b[0][1], j);
					chkmin(b[1][0], k);
					chkmax(b[1][1], k);
				}
				else if (s[j][k] == '?') {
					chkmin(x[j][0], k);
					chkmax(x[j][1], k);
					chkmin(most[0][0], j);
					chkmax(most[0][1], j);
					chkmin(most[1][0], k);
					chkmax(most[1][1], k);
				}
			}
			if (x[j][0] != N + 1) pts.pb({j, x[j][0]});
			if (x[j][1] != 0) pts.pb({j, x[j][1]});
		}
		for (int m = 0; m < 2; m++)
			for (int n = 0; n < 2; n++) {
				for (auto v : pts) {
					int idx = v.fi; if (m == 1) idx = v.se;
					if (idx == most[m][n]) {
						bds.pb(v);
						break;
					}
				}
			}
 		auto calc = [&](vector<pi> pts) {
			int bx[2][2];
			for (int i = 0; i < 2; i++)
				for (int j = 0; j < 2; j++)
					bx[i][j] = b[i][j];
			for (auto u : pts) {
				int x = u.fi, y = u.se;
				chkmin(bx[0][0], x);
				chkmax(bx[0][1], x);
				chkmin(bx[1][0], y);
				chkmax(bx[1][1], y);
			}
			return 1ll * (bx[0][1] - bx[0][0] + 1) * (bx[1][1] - bx[1][0] + 1);
		};
		ll area = 0;
		if (K >= 4) 
			area = calc(bds);
		else if (K == 1) {
			for (auto v : pts)
				chkmax(area, calc({v}));
		}
		else if (K == 2) {
			for (int i = 0; i < pts.size(); i++)
				for (int j = i; j < pts.size(); j++) 
					chkmax(area, calc({pts[i], pts[j]}));
		}
		else if (K == 0) {
			area = calc(vector<pi>());
		}
		else {
			for (auto v : pts) 
				for (auto u : bds)
					for (auto w : bds)
						chkmax(area, calc({v, u, w}));
		}
		cout << "Case #" << i << ": " << area << endl;
	}
	return 0;
}