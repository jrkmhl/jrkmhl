

def solution(A):
    # Implement your solution here
    sm = 0
    for e in A:
        sm = sm + e

    running_sm = 0
    n = len(A)
    i = 0
    res = float('inf')

    while i < n:
        running_sm = running_sm + A[i]
        sm = sm - A[i]
        res = min(res, abs(running_sm - sm))
        i += 1
    return res


# def solution(A):
#     # Implement your solution here
#     n = len(A)
#     right_sum = 0
#     for i in range(1, n):
#         right_sum = right_sum + A[i]
#
#     left_sum = A[0]
#
#     mn_diff = abs(left_sum - right_sum)
#
#     for i in range(1, n):
#         mn_diff = min(mn_diff, abs(left_sum - right_sum))
#         left_sum = left_sum + A[i]
#         right_sum = right_sum - A[i]
#
#     return mn_diff
