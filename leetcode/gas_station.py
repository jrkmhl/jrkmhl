def canCompleteCircuit(gas: list[int], cost: list[int]):
    n = len(gas)
    mx = -1

    for i in range(n):
        fuel = gas[i] - cost[i]

        if fuel >= 0:
            next_point = i + 1 if i != n - 1 else 0
            while next_point != i:
                fuel = fuel + gas[next_point] - cost[next_point]
                next_point = next_point + 1 if next_point != n - 1 else 0
            mx = max(mx, fuel)

    print(mx)


canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
# canCompleteCircuit([2, 3, 4], [3, 4, 3])
# canCompleteCircuit([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9])
