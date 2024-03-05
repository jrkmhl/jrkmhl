class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def reverse(i, j):
            while i < j:
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i += 1
                j -= 1

        while k > n:
            k = k - n

        # for i in range(k):
        #     last_element = nums[n-1]
        #     i = 0
        #     t1 = nums[i]
        #     while i+1<n:
        #         t2 = nums[i+1]
        #         nums[i+1] = t1
        #         t1 = t2
        #         i += 1
        #     nums[0]=last_element

        reverse(0, n - k - 1)
        reverse(n - k, n - 1)
        reverse(0, n - 1)




