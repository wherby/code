

# Create sub tree hash fun:

https://leetcode.com/problems/delete-duplicate-folders-in-system/

create trie like tree:
```
tree = {}
for path in paths:
    node = tree
    for folder in path:
        if folder not in node:
            node[folder] ={}
        node = node[folder]

#input paths=[["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
#tree {'a': {'b': {'x': {'y': {}}}}, 'c': {'b': {}}, 'w': {'y': {}}}
```

hash sub-tree:
```
def dfs(node,node_key,parent):
    child_tuple = tuple(dfs(node[key],key,node) for key in sorted(node.keys()))
    child_hash = hash(child_tuple)
    if child_tuple:
        child_hashes[child_hash].append((parent,node_key))
    return hash((child_hash,node_key))
```

print all tree path from root:
```
def dfs_collect_path(node,current,res):
    for key in node.keys():
        res.append(current + [key])
        dfs_collect_path(node[key],current + [key],res)
    return res
```