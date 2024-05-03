def maxSelectedElements(nums: list[int]) -> int:
    nums.sort()
    dp = [1] * len(nums)
    mx = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            dp[i] = dp[i - 1] + dp[i]
        mx = max(mx, dp[i])

    for i in range(len(nums)):
        temp_nums = increment_num(nums, i)
        temp_nums.sort()
        dp = [1] * len(nums)
        for i in range(1, len(temp_nums)):
            if nums[i] == nums[i - 1] + 1:
                dp[i] = dp[i - 1] + dp[i]
            mx = max(mx, dp[i])

    return mx


def increment_num(nums, i):
    nums[i] += 1
    return nums


res = maxSelectedElements([2,1,5,1,1])
print(res)