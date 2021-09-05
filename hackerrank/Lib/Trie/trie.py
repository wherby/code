import collections
words= ['foo', 'bar', 'baz', 'barz']

Trie = lambda: collections.defaultdict(Trie)
trie = Trie()
END = True

for i, word in enumerate(words):
    reduce(dict.__getitem__, word, trie)[END] = i
print trie