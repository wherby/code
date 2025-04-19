# Java

## set and array
```java
int[][] ans = new int[m][n];
Set<Integer> st = new HashSet<>();
st.clear();
st.add(grid[x][y]);



List<Integer>[] divisors = new ArrayList[MX];
Arrays.setAll(divisors, i -> new ArrayList<>());

Arrays.sort(nums);
int r = lowerBound(nums, j, upper - nums[j] + 1);
int l = lowerBound(nums, j, lower - nums[j]);

```

## String

```java
char[] s = S.toCharArray();
int n = s.length;

int cnt = (int) s.chars().distinct().count();

(int) s.chars().filter(c -> c == letter).count() * 100 / s.length();
```

## Map

Map<Integer, Integer> cnt = new HashMap<>();
int c = cnt.getOrDefault(x, 0);
cnt.put(x, c + 1);
