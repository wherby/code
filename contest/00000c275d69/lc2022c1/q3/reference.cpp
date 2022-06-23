//From https://leetcode-cn.com/contest/season/2022-spring/ranking/solo/ OTTFF question 3
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct SegT {
  vector<int> sum, ass;
  
  SegT(int n) : sum(n << 2), ass(n << 2) {
  }
  
  void apply_ass(int o, int v, int l, int r) {
    ass[o] = v;
    sum[o] = v * (r - l + 1);
  }
  void push(int o, int l, int m, int r) {
    if (ass[o] != -1) {
      apply_ass(o << 1, ass[o], l, m);
      apply_ass(o << 1 | 1, ass[o], m + 1, r);
      ass[o] = -1;
    }
  }
  void pull(int o) {
    sum[o] = sum[o << 1] + sum[o << 1 | 1];
  }
  
  // ----------------------------------------------------------------------------
  int L, R, V;
  void update(int o, int l, int r) {
     // cout << l << " " << r << endl;
    if (L <= l && r <= R) {
      apply_ass(o, V, l, r);
      return;
    }
    int m = (l + r) >> 1;
    push(o, l, m, r);
    if (L <= m) {
      update(o << 1, l, m);
    }
    if (m < R) {
      update(o << 1 | 1, m + 1, r);
    }
    pull(o);
  }
};

template<typename T,
         int IdFrom=0,
         typename OpLs=less<T>,
         typename OpEq=equal_to<T>>
struct Dctz {
    static OpLs ls;
    static OpEq eq;
    vector<T> x;
    void clear() { x.clear(); }
    void add(T v) { x.push_back(v); }
    void init() { 
        sort(x.begin(),x.end(),ls); 
        x.erase(unique(x.begin(),x.end(),eq),x.end()); 
    }
    int size() { return x.size(); }
    int id(const T &v) { 
        return lower_bound(x.begin(),x.end(),v,ls)-x.begin()+IdFrom; }
    int id2(const T &v) { 
        return upper_bound(x.begin(),x.end(),v,ls)-x.begin()-1+IdFrom; }
    T& operator[](int id) { return x[id-IdFrom]; };
};
Dctz<int> dc;

class Solution {
public:
    void dfs(TreeNode *u) {
        if (u == nullptr) return;
        dfs(u->left);
        dc.add(u->val);
        dfs(u->right);
    }
    int getNumber(TreeNode* root, vector<vector<int>>& ops) {
        dc.clear();
        dfs(root);
        dc.init();
        int m = dc.size();
        SegT segt(m);
        for (auto && op : ops) {
            segt.L = dc.id(op[1]);
            segt.R = dc.id2(op[2]);
            segt.V = op[0];
            segt.update(1, 0, m - 1);
        }
        return segt.sum[1];
    }
};