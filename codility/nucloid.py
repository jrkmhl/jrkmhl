def solution(S, P, Q):
    N = len(S)
    M = len(P)

    # Preprocess the DNA sequence to calculate prefix sums of impact factors
    impact_factors = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    prefix_sums = [[0] * (N + 1) for _ in range(4)]
    for i in range(N):
        for nucleotide, factor in impact_factors.items():
            print(prefix_sums[factor - 1][i])
            print((S[i] == nucleotide))
            prefix_sums[factor - 1][i + 1] = prefix_sums[factor - 1][i] + (S[i] == nucleotide)
    print(S)
    print(P)
    print(Q)
    print(prefix_sums)

    # For each query, find the minimal impact factor within the specified range
    result = []
    for i in range(M):
        start = P[i]
        end = Q[i] + 1
        for factor in range(4):
            if prefix_sums[factor][end] - prefix_sums[factor][start] > 0:
                result.append(factor + 1)
                break

    return result


# Example usage:
S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))  # Output: [2, 4, 1]
