# Backtracking

### Can write the generic backtracking skeleton (choose, recurse, undo) from memory
```
result, sol = [], []

backtrack(i):
    Base condition

    # Backtrack
    backtrack(i+1)

    # Picked picked
    Add to sol
    
    # Backtrack
    backtrack(i+1)

    # UNDO
    POP from sol

backtrack(0)
return result
```

---

### Can explain how Subsets II skips duplicate branches

By `sorting` the given array in ascending order, we can efficiently skip `duplicates` with the help of `while` loop.

Just start loop with `i+1` index & increment new index `index` if number at indice `i` & `index` are same.

---

### Attempted N-Queens and can explain the column and diagonal constraints

We have to use `loop` for traversal and checking for `columns`.

For `diagonals`, we will only check `UPPER-LEFT` & `UPPER-RIGHT` bcz `LOWER-LEFT` & `LOWER-RIGHT` will be checked by next `row` traversal.