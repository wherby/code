//https://leetcode.com/problems/online-majority-element-in-subarray/discuss/1174711/C%2B%2B-segment-tree
class MajorityChecker {
    const int kMax = 2e4+5;
    struct Node {
        int majority;  // majority number in a range
        int count;  // voting count, not total count in a range
    };
    int n;
    vector<Node> tree;
    vector<int> nums;
    vector<vector<int>> indice;

    // Boyer-Moore voting
    Node merge(const Node& a, const Node& b) {
        if (a.majority == b.majority) return {a.majority, a.count + b.count};
        if (a.count > b.count) return {a.majority, a.count - b.count};
        return {b.majority, b.count - a.count};
    }

    // build tree[i] with range [l, r]
    void build(int i, int l, int r) {
        if (l == r) {  // leaf node
            tree[i] = {nums[l-1], 1}; // remember range starts from index 1
            return;
        }
        int mid = l+(r-l)/2;
        build(i*2, l, mid);
        build(i*2+1, mid+1, r);
        // the push_up operation when build/update a segment tree
        tree[i] = merge(tree[i*2], tree[i*2+1]);
    }

    // for tree[i] with range [l, r], and a query [L, R],
    // return the majority number and its count
    Node query_majority(int i, int l, int r, int L, int R) {
        if (L > r || R < l) return {0, 0};
        if (L <= l && R >= r) return tree[i];
        int mid = l+(r-l)/2;
        Node a = query_majority(i*2, l, mid, L, R);
        Node b = query_majority(i*2+1, mid+1, r, L, R);
        return merge(a, b);
    }

public:
    MajorityChecker(vector<int>& arr) {
        n = arr.size();
        // usually 4*N is enough for building a segment tree
        tree.resize(kMax<<2);
        nums = arr;
        indice.resize(kMax);
        for (int i = 0; i < n; ++i) indice[arr[i]].push_back(i);
        build(1, 1, n);
    }

    int query(int left, int right, int threshold) {
        // find the majority number candidate
        int num = query_majority(1, 1, n, left+1, right+1).majority;
        if (num == 0) return -1;
        // although it's a majority number, we also have to check if its occurrences is >= threshold
        // that's why we need indice and binary search
        const auto& ni = indice[num];
        int l = lower_bound(ni.begin(), ni.end(), left)-ni.begin();
        int r = upper_bound(ni.begin(), ni.end(), right)-ni.begin();
        if (r-l >= threshold) return num;
        return -1;
    }
};