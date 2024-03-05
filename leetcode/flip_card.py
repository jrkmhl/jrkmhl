def flipgame(fronts: list[int], backs: list[int]) -> int:
    n = len(fronts)
    m = 9999999999
    print("start :")
    print("front:", fronts)
    print("back:", backs)
    for i in range(n):
        ft = fronts[i]
        bt = backs[i]
        m = min(m, find_min(i, fronts, backs))
        fronts[i] = ft
        backs[i] = bt

        print("After find_min:")
        print("front:", fronts)
        print("back:", backs)

        # print(m)

    # print(m)
    if m == 9999999999:
        return 0
    return m


def find_min(i, fronts1, backs1):
    print("Iteration --------:",i)
    print("fronts1:",fronts1)
    print("backs1:", backs1)
    # swap
    t = fronts1[i]
    fronts1[i] = backs1[i]
    backs1[i] = t
    m = 9999999999
    print("After swap :")
    print("fronts1:", fronts1)
    print("backs1:", backs1)
    for num in backs1:
        if num not in fronts1:
            m = min(m, num)
    return m


flipgame([1, 1], [2, 1])
