def countSubmatrices(grid: list[list[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])
    c = 0
    sm = 0
    # for first row

    for i in range(n):
        sm = sm + grid[0][i]
        if sm <= k:
            c += 1
    # for first column
    if m == 2 and n == 1:
        return c
    sm = 0
    for i in range(1, m):
        sm = sm + grid[i][0]
        if sm <= k:
            c += 1

    if m == 1 or n == 1:
        return c

    i = 2
    row_flag = False
    column_flag = False
    if m == 2 and n > 2:
        row_flag = True
        i = 1
    while i < m:
        j = 2
        if n == 2 and m > 2:
            j = 1
            column_flag = True

        while j < n:
            sm = 0
            i_range = i + 1 if row_flag else i
            for p in range(i_range):
                j_range = j + 1 if column_flag else j
                for q in range(j):
                    sm = sm + grid[p][q]
            if sm <= k:
                c += 1
            j += 1
        i += 1
    print(c)
    return c

# countSubmatrices([[7,6,3],[6,6,1]],18)
# countSubmatrices([[7,2,9],[1,5,0],[2,6,6]],20)
res =countSubmatrices([[6],[5]],9)
print(res)