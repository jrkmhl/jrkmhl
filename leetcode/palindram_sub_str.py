def countSubstrings(s: str):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    i = 0
    j = 1
    while j < n:
        if s[i] == s[j]:
            dp[i][j] = 1
        i += 1
        j += 1

    l = 2

    while l < n:
        start = 0
        end = l
        while start < n and end < n:
            if start + 1 < n and dp[start + 1][end - 1] == 1 and s[start] == s[end]:
                dp[start][end] = 1
            start += 1
            end += 1
        l = l + 1

    res = 0
    print(dp)
    for i in range(n):
        for j in range(n):
            if dp[i][j] == 1:
                res = res + 1
    print(res)


countSubstrings('aaaaa')
