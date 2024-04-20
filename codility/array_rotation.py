# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    if len(A)==0 or K==0:
        return A
    n = len(A)
    K = K % n
    A = reverse(A, 0, n - 1)
    A = reverse(A, 0, K - 1)
    A = reverse(A, K, n - 1)
    return A


def reverse(nums, i, j):
    while i <= j:
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t
        i += 1
        j -= 1
    return nums

