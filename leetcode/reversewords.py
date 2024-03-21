def reverseWords(self,s: str) -> str:
    n = len(s)
    i = n - 1
    while s[i] == ' ':
        i -= 1
    j = i
    res = ""
    print(i)
    print(j)
    while i >= 0:
        while i >= 0 and s[i] != ' ':
            i -= 1
        res = res + s[i + 1:j + 1] + " "
        # print(res)

        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i
        # i -= 1
    print(res)
    print(i)
    print(j)
    return res


reverseWords("the sky is blue")
