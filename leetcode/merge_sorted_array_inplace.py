class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n
        x = 0
        y = 0
        i = 0
        j = 0
        k = 0
        while k < l and x < m and y < n:
            if nums1[i] < nums2[j]:
                i = i + 1
                k = k + 1
                x = x + 1
            elif nums1[i] >= nums2[j]:
                # shift
                q = i
                t1 = nums1[q]
                while q + 1 < l:
                    t2 = nums1[q + 1]
                    nums1[q + 1] = t1
                    t1 = t2
                    q = q + 1
                nums1[i] = nums2[j]
                j = j + 1
                i = i + 1
                k = k + 1
                y = y + 1

        if x == m:
            for e in nums2[j:n]:
                nums1[i] = e
                i = i + 1


n1 = [1, 2, 3, 0, 0, 0]

n2 = [2, 5, 6]
m = 3
n = 3
r = merge(n1, m, n2, n)
print(r)
