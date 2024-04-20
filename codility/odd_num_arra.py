def solution(A):
    # Implement your solution here
    hash_map = {}
    for e in A:
        hash_map[e] = hash_map.get(e, 0) + 1

    for e in A:
        if hash_map.get(e) % 2 != 0:
            return e


