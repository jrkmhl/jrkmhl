def solution(A):
    # Implement your solution here
    n = len(A)
    zero = 0
    c = 0
    for i in range(n):
        if A[i] == 0:
            zero += 1
        else:
            c = c + zero

    return c if c < 1000000000 else -1

