def minSubArrayLen(target: int, nums: list[int]):
    n = len(nums)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = nums[i]
    m = n
    for i in range(n):
        for j in range(i, n):
            if i != j:
                dp[i][j] = dp[i][j - 1] + nums[j]
                # if dp[i][j] >= target:
                # m = min(m, j - i)
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] >= target:
                m = min(m, 1 if i == j else j - i)
    res = 0 if dp[0][n - 1] < target else m
    print(res)


minSubArrayLen(1, [1,2,3,4,5])
