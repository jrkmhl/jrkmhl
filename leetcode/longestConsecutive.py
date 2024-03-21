def longestConsecutive(nums: list[int]) -> int:
    hash_map = {}

    for n in nums:
        if hash_map.get(n - 1) is not None:
            hash_map[n - 1] = hash_map.get(n - 1) + 1
            # hash_map[n] = hash_map.get(n,0) + 1
            # mx = max(mx, )
        elif hash_map.get(n + 1) is not None:
            hash_map[n + 1] = hash_map.get(n + 1) + 1
            # hash_map[n] = hash_map.get(n, 0) + 1
        elif hash_map.get(n) is None:
            hash_map[n] = 1
        else:
            hash_map[n] = hash_map.get(n) + 1

    # unique = hash_map.keys()
    m = max(list(hash_map.values()))
    print(hash_map)
    sm = 0
    for k,v in hash_map.items():
        if v == m:
            sm = sm+v
    print(sm)

longestConsecutive([100,4,200,1,3,2])
longestConsecutive([0,3,7,2,5,8,4,6,0,1])
