// https://leetcode.cn/discuss/post/3690685/di-452-chang-zhou-sai-by-leetcode-0z7s/
// #TIPS# 用整体贡献比局部贡献考虑的状态少

#define MAXA ((int) 1e5)
bool inited = false, flag[MAXA + 5];
// 预处理质数
void init() {
    if (inited) return;
    inited = true;
    flag[1] = true;
    for (int i = 2; i <= MAXA; i++) if (!flag[i]) for (int j = i * 2; j <= MAXA; j += i) flag[j] = true;
}

class Solution {
public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        init();
        int n = nums.size();

        // 线段树节点定义
        struct Node {
            int mx, lazy;

            void apply(int x) {
                mx += x;
                lazy += x;
            }
        } tree[n * 4 + 5];

        // 两个子节点合并成父节点
        auto merge = [&](Node nl, Node nr) {
            return Node {
                max(nl.mx, nr.mx),
                0
            };
        };

        // 线段树建树
        auto build = [&](this auto &&build, int id, int l, int r) -> void {
            if (l == r) tree[id] = Node {0, 0};
            else {
                int nxt = id << 1, mid = (l + r) >> 1;
                build(nxt, l, mid); build(nxt | 1, mid + 1, r);
                tree[id] = merge(tree[nxt], tree[nxt | 1]);
            }
        };

        // 懒标记下推
        auto down = [&](int id) {
            if (tree[id].lazy == 0) return;
            int nxt = id << 1;
            tree[nxt].apply(tree[id].lazy);
            tree[nxt | 1].apply(tree[id].lazy);
            tree[id].lazy = 0;
        };

        // 线段树区间加减
        auto modify = [&](this auto &&modify, int id, int l, int r, int ql, int qr, int qv) -> void {
            if (ql <= l && r <= qr) tree[id].apply(qv);
            else {
                down(id);
                int nxt = id << 1, mid = (l + r) >> 1;
                if (ql <= mid) modify(nxt, l, mid, ql, qr, qv);
                if (qr > mid) modify(nxt | 1, mid + 1, r, ql, qr, qv);
                tree[id] = merge(tree[nxt], tree[nxt | 1]);
            }
        };

        unordered_map<int, set<int>> pos;
        // 施加（k = 1）或撤回（k = -1）质数 x 的贡献
        auto apply = [&](int x, int k) {
            auto &st = pos[x];
            if (st.empty()) return;
            // 质数 x 第一次和最后一次出现的位置
            int l = *(st.begin()), r = *prev(st.end());
            // 分界点选在 [1, l] 和 [r + 1, n - 1] 只会让答案增加 1
            if (1 <= l) modify(1, 1, n - 1, 1, l, k);
            if (r + 1 <= n - 1) modify(1, 1, n - 1, r + 1, n - 1, k);
            // // 分界点选在 [l + 1, r] 能让答案增加 2
            if (l + 1 <= r) modify(1, 1, n - 1, l + 1, r, k * 2);
        };

        build(1, 1, n - 1);
        // 初始化已有的质数
        for (int i = 0; i < n; i++) if (!flag[nums[i]]) pos[nums[i]].insert(i);
        for (auto &p : pos) apply(p.first, 1);
        vector<int> ans;
        for (auto &qry : queries) {
            int idx = qry[0], x = qry[1];
            if (!flag[nums[idx]]) {
                // 先撤回 nums[idx] 原来的贡献
                apply(nums[idx], -1);
                // nums[idx] 不再出现在 idx
                pos[nums[idx]].erase(idx);
                // 再施加 nums[idx] 现在的贡献
                apply(nums[idx], 1);
            }
            nums[idx] = x;
            if (!flag[x]) {
                // 先撤回 x 原来的贡献
                apply(x, -1);
                // x 现在出现在 idx
                pos[x].insert(idx);
                // 再施加 x 现在的贡献
                apply(x, 1);
            }
            // 因为问的是全局最大值，直接拿线段树根节点的答案即可
            ans.push_back(tree[1].mx);
        }
        return ans;
    }
};