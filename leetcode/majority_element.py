def majorityElement(self, nums: list[int]) -> int:
    counter = {}
    max_number = nums[0]
    for n in nums:
        if counter.get(n):
            counter[n] = counter.get(n) + 1
        else:
            counter[n] = 1

        if counter[n] > n / 2.0:
            max_number = n
    return n
