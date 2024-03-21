def numTeams(ratings: list):
    n = len(ratings)
    res = 0
    for j in range(n):
        left_small = 0
        left_bigger = 0

        right_small = 0
        right_big = 0

        for i in range(j - 1, -1, -1):
            if ratings[i] < ratings[j]:
                left_small += 1
            else:
                left_bigger += 1
        for k in range(j + 1, n):
            if ratings[k] < ratings[j]:
                right_small += 1
            else:
                right_big += 1

        res = res+left_small*right_big+left_bigger*right_small

    print(res)

numTeams([2,5,3,4,1])
