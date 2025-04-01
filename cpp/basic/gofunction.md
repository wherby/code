# Go


## Array and set
```go
ans := make([][]int, m)
set := map[int]struct{}{}
clear(set)
set[grid[x][y]] = struct{}{}
topLeft := len(set)
```

## String
```go
n := len(s)


set := map[rune]struct{}{}
for _, c := range s {
    set[c] = struct{}{}
}
return len(set)

```

## String

```go
strings.Count(s, string(letter)) * 100 / len(s)

```