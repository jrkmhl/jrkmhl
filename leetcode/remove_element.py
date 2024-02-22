def removeElement(self, nums: list[int], val: int) -> int:
    if len(nums) == 2 and nums[0] != val and nums[1] == val:
        return 1
    if not nums:
        return 0
    i = 0
    n = len(nums)
    j = n - 1
    count = 0
    while i <= j:
        if nums[i] == val:
            while j >= 0 and i < j and nums[j] == val:
                j = j - 1
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            j = j - 1

        i = i + 1
    for c in nums:
        if c != val:
            count = count + 1

    return count


# removeElement([1], 1)
# removeElement([3, 3], 3)
removeElement([2,2,3], 2)

# removeElement([0,1,2,2,3,0,4,2],2)

# [0, 1, 2, 2, 3, 0, 4, 2]
