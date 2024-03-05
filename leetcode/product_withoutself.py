def productExceptSelf(nums: list[int]):
    n = len(nums)
    dp1 = [1 for _ in range(n + 1)]
    dp2 = [1 for _ in range(n + 1)]

    print(nums)
    for i in range(1, n + 1):
        dp1[i] = dp1[i - 1] * nums[i - 1]

    print(dp1)

    j = n - 1
    while j >= 0:
        dp2[j] = dp2[j + 1] * nums[j]
        j -=1

    print(dp2)

    print([dp1[i] * dp2[i] for i in range(n)])


productExceptSelf([2, 3, 4, 5])
