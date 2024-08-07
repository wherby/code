//https://cp-algorithms.com/graph/lca_tarjan.html
vector<vector<int>> adj;
vector<vector<int>> queries;
vector<int> ancestor;
vector<bool> visited;

void dfs(int v)
{
    visited[v] = true;
    ancestor[v] = v;
    for (int u : adj[v]) {
        if (!visited[u]) {
            dfs(u);
            union_sets(v, u);
            ancestor[find_set(v)] = v;
        }
    }
    for (int other_node : queries[v]) {
        if (visited[other_node])
            cout << "LCA of " << v << " and " << other_node
                 << " is " << ancestor[find_set(other_node)] << ".\n";
    }
}

void compute_LCAs() {
    // initialize n, adj and DSU
    // for (each query (u, v)) {
    //    queries[u].push_back(v);
    //    queries[v].push_back(u);
    // }

    ancestor.resize(n);
    visited.assign(n, false);
    dfs(0);
}

find loerst common ancestor offline search
https://www.geeksforgeeks.org/tarjans-off-line-lowest-common-ancestors-algorithm/
https://www.geeksforgeeks.org/find-lca-in-binary-tree-using-rmq/





//https://codeforces.com/blog/entry/53738
   function TarjanOLCA(u)
    	MakeSet(u);
    	u.ancestor := u;
    	for each v in u.children do
    		TarjanOLCA(v);
    		Union(u,v);
    		Find(u).ancestor := u;
    	u.colour := black;
    	for each v such that {u,v} in P do	
    		if v.colour == black
    			print "Tarjan's Lowest Common Ancestor of " + u +
    				" and " + v + " is " + Find(v).ancestor + ".";