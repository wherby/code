# rolling hash
 https://leetcode-cn.com/problems/longest-duplicate-substring/submissions/

1. rabin-karp method(2 hash)
# https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode-0i9rd/

2. use good hash key
# use mod =2**64 k =131 or 13331
![rolling hash](./pic/rollinghash.png)


## Don't map 'a' to 0
https://wherby.github.io/code/string/string-hashing.html
Here is an example of calculating the hash of a string , which contains only lowercase letters. We convert each character of  to an integer. Here we use the conversion a->1 ,b->2 ,z->26 , . Converting a->0 is not a good idea, because then the hashes of the strings  a, aa,aaa ,  all evaluate to 0.


long long compute_hash(string const& s) {
    const int p = 31;
    const int m = 1e9 + 9;
    long long hash_value = 0;
    long long p_pow = 1;
    for (char c : s) {
        hash_value = (hash_value + (c - 'a' + 1) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    }
    return hash_value;
}