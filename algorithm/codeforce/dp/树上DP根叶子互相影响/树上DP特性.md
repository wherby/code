

# 
https://codeforces.com/contest/2167/problem/F
https://www.youtube.com/watch?v=lgPxucqRazM

已知一颗树，用任意点做数的根，然后把出现k个节点的lca的节点点记录下来记作Sr,
求所有点都做顶点的情况中 所有情况下可以被当lca点的总和 

用贡献法解决了换根的问题,贡献法求解当前节点可以被选中多少次，如果当前子树节点大于等于k，则当前子树作为子树的情况都符合，如果上半部分的节点大于等于k，则当前子树作为上半部分子树的情况都符合，然后加上自身
对于树上的每一点，都可以分为上下两半的子树，在换根的时候，会以上下两半子树作为当前点的子树

 贡献计算的主循环循环遍历每个节点 $i$ 并计算其总贡献 $\text{Contribution}(i)$：$$\text{Contribution}(i) = 1 + \mathbb{I}(\text{sz}[i] \ge k) \cdot (n - \text{sz}[i]) + \mathbb{I}(n - \text{sz}[i] \ge k) \cdot \text{sz}[i]$$

该公式利用了 $\text{sz}[i]$ 和 $n-\text{sz}[i]$ 这两个值，将所有 $n$ 个可能的根 $r$ 分成三类，恰好实现了换根法：| 根 $r$ 的位置 | 根的数量 | 节点 $i$ 的有效子树大小 $|B|$ | 贡献计算 || :--- | :--- | :--- | :--- || $r = i$ | $1$ | $n-1$ | + 1 (特殊处理，通常需要 $\mathbb{I}(n-1 \ge k)$) || $r \in i$ 的子树 (DFS子节点方向) | $\text{sz}[i]$ | $n - \text{sz}[i]$ | $\mathbb{I}(n - \text{sz}[i] \ge k) \cdot \text{sz}[i]$ || $r \in i$ 的外部 (DFS父节点方向) | $n - \text{sz}[i]$ | $\text{sz}[i]$ | $\mathbb{I}(\text{sz}[i] \ge k) \cdot (n - \text{sz}[i])$ |公式解读：ans += sz[i]：当根 $r$ 位于 $i$ 的子树内（共 $\text{sz}[i]$ 个点）时， $i$ 的有效子树是外部 $n-\text{sz}[i]$。只有当 $n-\text{sz}[i] \ge k$ 时，才将 $\text{sz}[i]$ 次贡献累加进来。ans += n - sz[i]：当根 $r$ 位于 $i$ 的外部（共 $n-\text{sz}[i]$ 个点）时，$i$ 的有效子树是子树 $\text{sz}[i]$。只有当 $\text{sz}[i] \ge k$ 时，才将 $n-\text{sz}[i]$ 次贡献累加进来。ans++：这是对 $r=i$ 情况的简化处理，即 $r=i$ 时，只要 $n-1 \ge k$，贡献就为 $1$。通过这种方式，代码利用了初始 $\text{DFS}$ 的结果 $\text{sz}[i]$，巧妙地将所有 $n$ 种可能的根 $r$ 的情况都分类讨论并求和，从而避免了多次 $\text{DFS}$ 或复杂的 $\text{LCA}$ 组合公式。总结：该代码是正确的，因为它成功地将复杂的 LCA 集合计数问题，简化为了 $\mathbf{|B| \ge k}$ 的连通分量大小判断，并通过一次 $\text{DFS}$ 的结果实现了所有 $n$ 个根的贡献求和。


问题描述
Behruzbek 得到一棵包含 *n* 个节点的树（无环连通无向图）。

如果选定一个节点 *r* 作为树的根，那么对于树中任意 *k* 个互不相同的节点构成的集合，可以计算它们在以 *r* 为根的树中的最低公共祖先（LCA）。

把所有这样的 *k*-节点集合的 LCA 收集起来（去重），得到的节点集合记作 Sᵣ。
定义该树在根 *r* 下的 可爱度（cuteness） 为 |Sᵣ|（即 Sᵣ 中不同节点的个数）。

在了解了可爱度之后，Behruzbek 想定义树的 萌值（kawaiiness） 为：


 ∣
也就是分别以每个节点为根，计算可爱度，然后把所有可爱度加起来。

现在给定树的结构和整数 *k*，请你帮助 Behruzbek 计算出这棵树的萌值。

``` cpp
#include <bits/stdc++.h>
using namespace std;
 
using i64 = long long;
 
int main() {
    cin.tie(nullptr)->sync_with_stdio(false);
 
    auto solve = [&]() {
        int n, k;
        cin >> n >> k;
 
        vector<vector<int>> adj(n);
        for (int i = 0; i < n - 1; i++) {
            int u, v;
            cin >> u >> v;
            u--, v--;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
 
        vector<int> sz(n, 1);
        [&](this auto &&dfs, int u, int p) -> void {
            for (auto v : adj[u]) {
                if (v != p) {
                    dfs(v, u);
                    sz[u] += sz[v];
                }
            }
        }(0, -1);
 
        i64 ans = 0;
 
        for (int i = 0; i < n; i++) {
            ans++;
            if (sz[i] >= k) {
                ans += n - sz[i];
            }
            if (n - sz[i] >= k) {
                ans += sz[i];
            }
        }
 
        cout << ans << '\n';
    };
 
    int t;
    cin >> t;
 
    while (t--) {
        solve();
    }
    
    return 0;
}
```