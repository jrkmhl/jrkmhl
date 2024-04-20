def solution(N, A):
    # Implement your solution here
    res = [0] * N
    mx = 0

    last_max = 0

    for x in A:
        if 1 <= x <= N:
            res[x - 1] = max(res[x - 1], last_max)
            res[x - 1] += 1
            mx = max(res[x - 1], mx)
        elif x == N + 1:
            last_max = mx

    for i in range(N):
        res[i] = max(res[i], last_max)

    return res
