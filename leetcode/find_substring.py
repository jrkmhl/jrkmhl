def findSubstring(s: str, words: list[str]) -> list[int]:
    word_len = len(words[0])
    words_len = len(words)
    hash_map = {}
    for w in words:
        hash_map[w] = hash_map.get(w, 0) + 1

    i = 0
    n = len(s)
    res = []
    while i < n:
        win = i + words_len * word_len - 1
        j = i
        hash_set = {}
        while j <= win and win < n:
            tmp = s[j:(j + word_len)]
            if tmp in words:
                hash_set[tmp] = hash_set.get(tmp, 0) + 1
            j = j + word_len
        flag = False
        for word in words:
            if hash_map[word] != hash_set.get(word, 0) and not flag:
                flag = True
        if not flag:
            res.append(i)
        i = i + 1
    print(res)
    return res


findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"])
