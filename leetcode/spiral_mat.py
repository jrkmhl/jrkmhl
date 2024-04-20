def spiralOrder(matrix) -> list[int]:
    m = len(matrix)
    n = len(matrix[0])
    res = []
    top = 0
    bottom = m - 1
    left = 0
    right = n - 1
    c = 0
    while c <= m * n:
        i = left
        while i <= right:
            res.append(matrix[left][i])
            i += 1
            c += 1
        top = top + 1
        if c == m * n:
            break
        i = top
        while i <= bottom:
            res.append(matrix[i][right])
            i += 1
            c += 1
        right = right - 1

        if c == m * n:
            break
        i = right
        while i >= left:
            res.append(matrix[bottom][i])
            i -= 1
            c += 1
        if c == m * n:
            break
        bottom = bottom - 1

        i = bottom

        while i >= top:
            res.append(matrix[i][left])
            i = -1
            c += 1
        left = left + 1

        print(res)

    return res


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(spiralOrder(mat))
