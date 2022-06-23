#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) {fprintf(stderr, __VA_ARGS__);fflush(stderr);}
#else
	#define eprintf(...) 42
#endif

using ll = long long;
using ld = long double;
using uint = unsigned int;
using ull = unsigned long long;
template<typename T>
using pair2 = pair<T, T>;
using pii = pair<int, int>;
using pli = pair<ll, int>;
using pll = pair<ll, ll>;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
ll myRand(ll B) {
	return (ull)rng() % B;
}

#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second

clock_t startTime;
double getCurrentTime() {
	return (double)(clock() - startTime) / CLOCKS_PER_SEC;
}

void solve() {
	int n, k;
	scanf("%d%d", &n, &k);
	if (k < n - 1 || k % 2 == 1) {
		printf("IMPOSSIBLE\n");
		return;
	}
	vector<pii> ans;
	k -= n - 1;
	int X = 1;
	int d = n;
	while(true) {
		d--;
		if (k < d) {
			X += d / 2;
			X += k / 2;
			while(k < d) {
				int Y = X + 4 * d - 1;
				ans.push_back(mp(X, Y));
				X = Y;
				d -= 2;
			}
			X += d / 2;
			while(d > 0) {
				int Y = X + 4 * d - 3;
				ans.push_back(mp(X, Y));
				X = Y;
				d -= 2;
			}
			break;
		} else {
			k -= d;
			X += d;
		}
		if (k < d) {
			X += d / 2;
			X += k / 2;
			while(k < d) {
				int Y = X + 4 * d - 3;
				ans.push_back(mp(X, Y));
				X = Y;
				d -= 2;
			}
			X += d / 2;
			while(d > 0) {
				int Y = X + 4 * d - 5;
				ans.push_back(mp(X, Y));
				X = Y;
				d -= 2;
			}
			break;
		} else {
			k -= d;
			X += d;
		}
		if (k < d) {
			X += d / 2;
			X += k / 2;
			while(k < d) {
				int Y = X + 4 * d - 5;
				ans.push_back(mp(X, Y));
				X = Y;
				d -= 2;
			}
			X += d / 2;
			while(d > 0) {
				int Y = X + 4 * d - 7;
				if (X + 1 < Y) ans.push_back(mp(X, Y));
				X = Y;
				d -= 2;
			}
			break;
		} else {
			k -= d;
			X += d;
		}
		if (k + 2 < d) {
			X += d / 2;
			X += k / 2;
			while(k + 2 < d) {
				int Y = X + 4 * d - 7;
				ans.push_back(mp(X, Y));
				X = Y;
				d -= 2;
			}
			X++;
			k += 2;
			d -= 2;
			X += d / 2;
			while(d > 0) {
				int Y = X + 4 * d - 1;
				if (X + 1 < Y) ans.push_back(mp(X, Y));
				X = Y;
				d -= 2;
			}
			break;
		} else {
			k -= d;
			X += d;
		}
		k += 2;
		d--;
	}
	assert(X == n * n);
	printf("%d\n", (int)ans.size());
	for (pii t : ans) printf("%d %d\n", t.first, t.second);
}

int main()
{
	startTime = clock();
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
