# from collections import
def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    res = []
    n = len(words)
    i = 0
    while i < n:
        j = i
        l = 0
        while i < n and l <= maxWidth:
            if l == 0:
                l = l + len(words[i])
            else:
                l = l + len(words[i]) + 1
            i += 1
        print(l)
        num_spaces = maxWidth - l
        res.append(" ".join(words[j:i + 1]))
        i += 1

    print(res)

    return res


fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
