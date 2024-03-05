def maxLengthBetweenEqualCharacters(s: str) -> int:
    n = len(s)
    i = 0
    h = {}
    longest = -1
    while i < n:
        if h.get(s[i]) is None:
            h[s[i]] = i
        else:
            longest = max(longest, (i + 1) - h.get(s[i]))
            h[s[i]] = i
        i += 1
        print(h)
    print(longest)

    return longest


maxLengthBetweenEqualCharacters("abca")
