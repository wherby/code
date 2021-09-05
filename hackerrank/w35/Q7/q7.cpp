#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)

using namespace std;

/*************************************************************************/

void multisetRemove(int x, multiset <int> &values) {
    values.erase(values.find(x));
}

/* Just take the prev() of an iterator, but take into account .begin() */
set <int>::iterator safePrev(set <int>::iterator &it, multiset <int> &s) {
    if (it == s.begin()) {
        return s.end();
    } else {
        return prev(it);
    }
}

/* Add x to [values], updating the set of differences [diffs] */
void setDiffsAdd(int x, multiset <int> &values, multiset <int> &diffs) {
    auto right = values.lower_bound(x);
    auto left = safePrev(right, values);
    
    if (left != values.end()) {
        diffs.insert(x - *left);
    }
    
    if (right != values.end()) {    
        diffs.insert(*right - x);
    }
    
    if (left != values.end() && right != values.end()) {
        multisetRemove(*right - *left, diffs);
    }
    
    values.insert(x);
}

/* Remove x from [values], updating the set of differences [diffs] */
void setDiffsRemove(int x, multiset <int> &values, multiset <int> &diffs) {
    auto it = values.find(x);
    auto left = safePrev(it, values);
    auto right = next(it);
    
    if (left != values.end()) {
        multisetRemove(x - *left, diffs);
    }
    
    if (right != values.end()) {
        multisetRemove(*right - x, diffs);
    }
    
    if (left != values.end() && right != values.end()) {
        diffs.insert(*right - *left);
    }
    
    multisetRemove(x, values);
}

/*************************************************************************/

vector <int> solve(int n, int d, vector <int> &xs) {
    vector <int> ans(n, 0);
    
    int first = xs[0];
    int low = first, high = first;
    
    multiset <int> airports = {first - d, first, first + d};
    multiset <int> diffs = {d, d};
    
    FOR(i,1,n-1) {
        int x = xs[i];
        
        int left = high - d;
        int right = low + d;
        
        setDiffsRemove(left, airports, diffs);
        setDiffsRemove(right, airports, diffs);
    
        low = min(low, x);
        high = max(high, x);

        left = high - d;
        right = low + d;
        
        setDiffsAdd(x, airports, diffs);
        
        while (!airports.empty() && *airports.begin() <= left) {
            setDiffsRemove(*airports.begin(), airports, diffs);
        }
        
        while (!airports.empty() && *airports.rbegin() >= right) {
            setDiffsRemove(*airports.rbegin(), airports, diffs);
        }
        
        setDiffsAdd(left, airports, diffs);
        setDiffsAdd(right, airports, diffs);
        
        /* One must be careful when high - low < d - then the boundary
           airports (in positions low and high) are inside
           the interval (left, right), but shouldn't be considered,
           so we temporarily remove them before checking the largest difference
        */
        if (high - low < d) {
            setDiffsRemove(low, airports, diffs);
            setDiffsRemove(high, airports, diffs);
        }
        
        ans[i] = max(0, d - (high - low));
        
        if (!diffs.empty()) {
            ans[i] = max(ans[i], (right - left) - *diffs.rbegin());
        }
        
        if (high - low < d) {
            setDiffsAdd(low, airports, diffs);
            setDiffsAdd(high, airports, diffs);
        }
    }
    
    return ans;
}

/*************************************************************************/

int main() {
    ios_base::sync_with_stdio(0);
    
    int t;
    cin >> t;
    
    while (t--) {
        int n, d;
        cin >> n >> d;
        
        vector <int> xs(n);
        FOR(i,0,n-1) {
            cin >> xs[i];
        }
        
        vector <int> ans = solve(n, d, xs);
        
        FOR(i,0,n-1) {
            cout << ans[i] << " \n"[i == n-1];
        }
    }

    return 0;
}

/*************************************************************************/