data Tree a = Leaf | Node (Tree a) a (Tree a) 
    deriving Show

insert :: (Ord a) => a -> Tree a -> Tree a
insert v Leaf = Node Leaf v Leaf
insert v (Node l vt r)
    | v <= vt = Node (insert v l) vt r
    | v > vt = Node l vt (insert v r)

inorder :: Tree a -> [a]
inorder Leaf = []
inorder (Node l v r)=
    (inorder l) ++ [v] ++ (inorder r)

