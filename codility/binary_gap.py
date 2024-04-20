# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    binary = []

    while N != 0:
        binary.append(N % 2)
        N = N // 2

    l = len(binary)
    c = 0
    i = 0
    res = 0
    while i < l:
        if binary[i] == 1:
            i += 1
            while i < l and binary[i] != 1:
                c += 1
                i += 1
            res = max(res, c)
            c = 0
        else:
            i += 1
    return res



