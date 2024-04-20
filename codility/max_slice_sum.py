# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    prev_max = A[0]
    curr_max = A[0]
    n = len(A)

    for i in range(1, n):
        curr_max = max(A[i], curr_max + A[i])
        prev_max = max(prev_max, curr_max)

    return prev_max
