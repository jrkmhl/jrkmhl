# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def sol(A):
    dp = [0]*6
    n = len(A)
    for i in range(0,n,2):
        pass



def solution(A):
    # Implement your solution here
    n = len(A)
    domino_seq = []
    i = 1
    while i < n:
        domino_seq.append((A[i - 1], A[i]))
        i += 2

    print(domino_seq)
    k = len(domino_seq)
    valid_dominos = 0

    visited = set()
    for i in range(k):
        for j in range(i + 1, k):
            s = domino_seq[i]
            t = domino_seq[j]
            if s[1] == t[0]:
                visited.add(s)
                visited.add(t)

    print(k - len(visited))
    print(domino_seq)
    print(visited)
    return k - len(visited)

solution([5, 1, 2, 6, 6, 1, 3, 1, 4, 3, 4, 3, 4, 6, 1, 2, 4, 1, 6, 2])
