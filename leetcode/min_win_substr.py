def minWindow(s: str, t: str) -> str:
    n = len(s)
    m = len(t)
    i = 0
    hash_map = {}
    l = 0
    mn = n
    res = ""
    for c in t:
        hash_map[c] = hash_map.get(c, 0) + 1

    while i < n:
        j = i
        k = i + m - 1
        min_found = False
        while k < n:
            hs = {}
            for c in s[j:k + 1]:
                hs[c] = hs.get(c, 0) + 1

            flag = True
            for c in t:
                if hash_map.get(c) != hs.get(c, 0) and flag:
                    flag = False
            if flag:
                if k - j < mn:
                    mn = k- j
                    res = s[j:k + 1]
                    min_found = True
            if min_found:
                break

            k += 1
        i += 1

    print(res)

    return res

minWindow("ADOBECODEBANC","ABC")