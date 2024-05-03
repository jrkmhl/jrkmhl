def alternatingSubarray(nums: list[int]) -> int:
    n = len(nums)

    i = 1
    prev = nums[1] - nums[0]
    c = 1  # if not prev  in (-1,1) else 1
    res = 0

    while i < n:
        curr = nums[i] - nums[i-1]
        if (prev == 1 and curr == -1) or (prev == -1 and curr == 1):
            c += 1
            res = max(res, c)
        else:
            c = 1
        i += 1
        prev = curr

    return res

alternatingSubarray([2,3,4,3,4])