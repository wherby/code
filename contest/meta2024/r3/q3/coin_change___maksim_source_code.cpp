/*
    author:  Maksim1744
    created: 02.11.2024 22:20:49
*/

#include "bits/stdc++.h"

using namespace std;

using ll = long long;
using ld = long double;

#define mp   make_pair
#define pb   push_back
#define eb   emplace_back

#define sum(a)     ( accumulate ((a).begin(), (a).end(), 0ll))
#define mine(a)    (*min_element((a).begin(), (a).end()))
#define maxe(a)    (*max_element((a).begin(), (a).end()))
#define mini(a)    ( min_element((a).begin(), (a).end()) - (a).begin())
#define maxi(a)    ( max_element((a).begin(), (a).end()) - (a).begin())
#define lowb(a, x) ( lower_bound((a).begin(), (a).end(), (x)) - (a).begin())
#define uppb(a, x) ( upper_bound((a).begin(), (a).end(), (x)) - (a).begin())

template<typename T>             vector<T>& operator--            (vector<T> &v){for (auto& i : v) --i;            return  v;}
template<typename T>             vector<T>& operator++            (vector<T> &v){for (auto& i : v) ++i;            return  v;}
template<typename T>             istream& operator>>(istream& is,  vector<T> &v){for (auto& i : v) is >> i;        return is;}
template<typename T>             ostream& operator<<(ostream& os,  vector<T>  v){for (auto& i : v) os << i << ' '; return os;}
template<typename T, typename U> pair<T,U>& operator--           (pair<T, U> &p){--p.first; --p.second;            return  p;}
template<typename T, typename U> pair<T,U>& operator++           (pair<T, U> &p){++p.first; ++p.second;            return  p;}
template<typename T, typename U> istream& operator>>(istream& is, pair<T, U> &p){is >> p.first >> p.second;        return is;}
template<typename T, typename U> ostream& operator<<(ostream& os, pair<T, U>  p){os << p.first << ' ' << p.second; return os;}
template<typename T, typename U> pair<T,U> operator-(pair<T,U> a, pair<T,U> b){return mp(a.first-b.first, a.second-b.second);}
template<typename T, typename U> pair<T,U> operator+(pair<T,U> a, pair<T,U> b){return mp(a.first+b.first, a.second+b.second);}
template<typename T, typename U> void umin(T& a, U b){if (a > b) a = b;}
template<typename T, typename U> void umax(T& a, U b){if (a < b) a = b;}

#ifdef HOME
#define SHOW_COLORS
#include "/mnt/c/Libs/tools/print.cpp"
#else
#define show(...) void(0)
#define debugf(fun)   fun
#define debugv(var)   var
#define mclock    void(0)
#define shows     void(0)
#define debug  if (false)
#define OSTREAM(...)    ;
#define OSTREAM0(...)   ;
#endif

const ld ga = 0.57721566490153286060;

ld harm(ld n) {
    return (ld)(log((ld)n) + ga);
}

void test_case(int test) {
    ll n;
    int p100;
    cin >> n >> p100;
    if (p100 == 0) {
        if (n < 1e8) {
            ld ans = 0;
            for (int k = 0; k < (int)n; ++k) {
                ans += (ld)n / (n - k);
            }
            cout << fixed << setprecision(20) << ans << '\n';
            // cout << fixed << setprecision(20) << ans << '\n';
            // cout << fixed << setprecision(20) << n * (log(n) + ga) << '\n';
            // cout << fixed << setprecision(20) << (n * (log(n) + ga) - ans) / ans << '\n';
        } else {
            cout << fixed << setprecision(20) << (ld)n * (log((ld)n) + ga) << '\n';
        }
    } else {
        int stop = 1;
        while ((stop - 1) * p100 < 100)
            ++stop;
        vector<int> inter = {1, stop - 1, stop};
        sort(inter.begin(), inter.end());
        inter.erase(unique(inter.begin(), inter.end()), inter.end());

        auto calc_exp = [&](ll k, int d) -> ld {
            ld s = (ld)(n - k) / n;
            ld cur;
            if ((d - 1) * p100 >= 100) {
                cur = d;
            } else {
                ld prob = (ld)(d - 1) * p100 / 100;
                cur = d / (prob + (1 - prob) * s);
            }
            return cur;
        };

        vector<ll> betweens;
        for (int i = 0; i + 1 < inter.size(); ++i) {
            ll l = 0, r = n;
            while (r - l > 1) {
                ll c = (l + r) / 2;

                if (calc_exp(c, inter[i]) < calc_exp(c, inter[i + 1])) {
                    l = c;
                } else {
                    r = c;
                }
            }
            betweens.pb(r);
        }
        betweens.pb(n);
        betweens.insert(betweens.begin(), 0);

        ld ans = 0;
        show(betweens);
        show(inter);
        for (int i = 0; i < inter.size(); ++i) {
            ll kl = betweens[i];
            ll kr = betweens[i + 1] - 1;
            if (kl > kr) {
                continue;
            }
            ld d = inter[i];
            if (i + 1 == inter.size()) {
                ans += (ld)d * (kr - kl + 1);
                continue;
            }
            ld p = (ld)(d - 1) * p100 / 100;
            if (kr - kl < 1e8) {
                for (ll k = kl; k <= kr; ++k) {
                    // ans += calc_exp(k, inter[i]);
                    ans += d * n / (k * (p - 1) + n);
                }
            } else {
                ld xl = -(kr - n / (1 - p));
                ld xr = -(kl - n / (1 - p));
                // show(xl, xr);

                ld cur = 0;
                cur = ((harm(xr + 1) - harm(xl)) + (harm(xr) - harm(xl - 1))) / 2;
                // for (ld u = xl; u <= xr; u += 1) {
                //     cur += 1 / u;
                // }
                ans += cur * d * n / (1 - p);
            }
        }

        cout << fixed << setprecision(20) << ans << '\n';
        // if (n > 1e8) return;
        // n = 1000;
        // for (int p100 = 1; p100 <= 100; ++p100) {
        //     cerr << "stop: " << stop << endl;
        //     ld p = (ld)p100 / 100;
        //     ld ans = 0;
        //     for (ll k = 0; k < n; ++k) {
        //         ld s = (ld)(n - k) / n;
        //         ld mn = n;
        //         int bestd = 1;
        //         for (int d = 1; d <= 101; ++d) {
        //             ld cur;
        //             if ((d - 1) * p100 >= 100) {
        //                 cur = d;
        //             } else {
        //                 ld prob = (ld)(d - 1) * p100 / 100;
        //                 cur = d / (prob + (1 - prob) * s);
        //             }
        //             if (cur < mn) {
        //                 bestd = d;
        //             }
        //             mn = min(mn, cur);
        //         }
        //         cerr << bestd << ' ';
        //         assert(bestd == 1 || bestd == stop || bestd == stop - 1);
        //         ans += mn;
        //     }
        //     cerr << endl;
        // }
        // exit(0);
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int test_count;
    cin >> test_count;
    for (int test = 1; test <= test_count; ++test) {
        cout << "Case #" << test << ": ";
        test_case(test);
    }

    return 0;
}
