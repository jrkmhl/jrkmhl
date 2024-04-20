def wordBreak(s: str, wordDict: list[str]) -> bool:
    # n= len(s)
    used = {}

    for w in wordDict:
        if len(s) == 0:
            return True
        if used.get(w, False):
            s = s[len(w):]
        elif is_str_starts_with(w, s):
            used[w] = True
            s = s[len(w):]
    if len(s) == 0:
        return True
    return False


def is_str_starts_with( w, s):
    if len(s) == 0:
        return True
    else:
        m = len(s)
        n = len(w)
        i = 0
        j = 0
        while i < m and j < n:
            if w[j] != s[i]:
                return False
            i += 1
            j += 1
        if j == n:
            return True
        return False

wordBreak("applepenapple",)