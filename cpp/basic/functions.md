

# Vector
```cpp
vector ans(m, vector<int>(n));
```

# set
```cpp
unordered_set<int> st;
st.insert(grid[x][y]);
st.clear();
st.size();
```

## string 
```cpp
int n = s.size();

int cnt = unordered_set(s.begin(), s.end()).size();


ranges::count(s, letter) * 100 / s.size()

```

## stack

```cpp
vector<int> stk = {n + 1};
stk.emplace_back(nums[i]);
while (!stk.empty() && stk.back() == cur) {
            stk.pop_back();
            cur ++;
        }
```
