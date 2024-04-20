# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    n = len(S)
    i = 0
    j = 0
    res = 0
    while j < n:
        while j < n and S[j] != ' ':
            j += 1
        x = is_valid(S, i, j - 1)
        # print(x)
        if x:
            res = max(res, j - i)
        j += 1
        i = j

    return res


def is_valid(s, i, j):
    # print(s[i:j+1])
    alfa = 0
    digi = 0
    special = 0

    while i <= j:
        if (ord("a") <= ord(s[i]) <= ord("z")) or (ord(s[i]) >= ord("A") >= ord(s[i])):
            alfa += 1
        elif ord("0") <= ord(s[i]) <= ord("9"):
            digi += 1
        else:
            special += 1
        i += 1

    if special > 0:
        return False
    if alfa % 2 == 0 and digi % 2 != 0:
        return True
    return False



print(solution('helloworld1'))

