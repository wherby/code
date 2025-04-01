# Java

## set and array
```java
int[][] ans = new int[m][n];
Set<Integer> st = new HashSet<>();
st.clear();
st.add(grid[x][y]);
```

## String

```java
char[] s = S.toCharArray();
int n = s.length;

int cnt = (int) s.chars().distinct().count();

(int) s.chars().filter(c -> c == letter).count() * 100 / s.length();
```