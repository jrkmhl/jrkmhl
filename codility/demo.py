# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    mx = max(A)
    if mx < 0:
        return 1
    hash_map = {}
    for e in A:
        hash_map[e] = True
    n = len(A)
    for i in range(1, n + 1):
        if not hash_map.get(i, False):
            return i
    return n + 1
