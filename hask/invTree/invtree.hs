data Tree a = Leaf | Node (Tree a) a (Tree a) 
    deriving Show
inv_tup_tree = aux (0,0)
    where 
        aux(l,r) = Node(aux $ (l+1,r)) (l,r) (aux $ (l, r+1))

cut :: Integer -> Tree a -> Tree a
cut 0 _ = Leaf
cut n Leaf = Leaf
cut n (Node l v r) = Node (cut (n-1) l) v (cut (n-1) r)