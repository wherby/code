# insect

https://stackoverflow.com/questions/29959506/is-there-a-go-analog-of-pythons-bisect-module

Yes. sort.Search() is what you want. It takes a length and a comparison function, and returns the first index for which the function returns true. The example in the linked docs includes:
```
i := sort.Search(len(data), func(i int) bool { return data[i] >= x })
```
That sets i to the index of the first value >= x (or to len(data) if no items are >= x), so it's like bisect.bisect_left() in Python. Change it to > to get something like bisect_right.

The Python functions will also search through a range within a list; to do something similar, you could search a subslice of your slice, and add its starting offset to the index Search returns if you need an index into the original slice. There are other ways, but that seems simple and readable.

Though this is also true of Python lists, insertion into a sorted slice is O(n), i.e., it averages twice as slow on twice as much data. That's still fine for many purposes (many times you have a small list or few inserts), but of course you can't scale indefinitely that way. If you're inserting a ton of items, like a significant fraction of the list size, you could append them all, then sort. For general sorted collections with logarithmic-time inserts, deletes, etc., there's always, for example, github.com/cznic/b, or any number of database-y things.