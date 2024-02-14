def func():
    s = "abcd"
    b = "bcdadfhhddhhhabcddhdhdhdabcd"
    # b = "cbabadcbbabbcbabaabccbabc"
    m = len(s)
    n = len(b)
    count = 0
    for i in range(n):
        window = i + m
        if window < n:
            flag = True
            for j in range(i, window, 1):
                is_char_match = False
                for k in range(m):
                    if b[j] == s[k]:
                        is_char_match = True
                        break
                if not is_char_match:
                    flag = False
            if flag:
                count = count + 1
    print(count)


def compare():
    s1 = "abcd"
    s2 = "aabc"
    m = len(s1)
    n = len(s2)
    flag = True
    for i in range(m):
        is_char_match = False
        for j in range(n):
            if s1[i] == s2[j]:
                is_char_match = True
                break
        if not is_char_match:
            flag = False

    if flag:
        print("matching")
    else:
        print("not matching")


def count_all_perm():
    s = "abbc"
    # b = "bcdadfhhddhhhabcddhdhdhdabcd"
    b = "cbabadcbbabbcbabaabccbabc"
    m = len(s)
    n = len(b)
    count = 0
    hash_map = {}
    for c in s:
        hash_map[c] = hash_map.get(c, 0) + 1

    for i in range(n):
        window = i + m
        if window <= n:
            is_anagram = True
            temp_hash_map = {}
            for j in range(i, window, 1):
                temp_hash_map[b[j]] = temp_hash_map.get(b[j], 0) + 1

            for each_char in s:
                if hash_map.get(each_char) != temp_hash_map.get(each_char, 0):
                    is_anagram = False
                    break
            if is_anagram:
                count = count + 1
        else:
            break

    print(count)


def permitate(s, fi):
    if fi == len(s):
        print(s)
        return
    else:
        for i in range(fi, len(s), 1):
            t = s[i]
            s[i] = s[fi]
            s[fi] = t
            permitate(s, fi + 1)
            t = s[i]
            s[i] = s[fi]
            s[fi] = t


def search(ele, arr, low, high):
    # low = 0
    # high = len(arr)

    # while low <= high:
    #     mid = int((low + high) / 2)
    #     if arr[mid] == ele:
    #         return True
    #     elif ele > arr[mid]:
    #         low = mid + 1
    #     elif ele < arr[mid]:
    #         high = mid - 1

    if low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == ele:
            return True
        elif ele < arr[mid]:
            return search(ele, arr, low, mid - 1)
        elif ele > arr[mid]:
            return search(ele, arr, mid + 1, high)

    return False


def common_ele():
    a = [13, 27, 35, 40, 70, 55, 59, 60]
    b = [17, 35, 39, 40, 55, 58, 60, 70]

    for num in a:
        if search(num, b, 0, len(b)):
            print(num)


def comm_ele1():
    a = [13, 27, 35, 40, 47, 59, 60, 70]
    b = [17, 35, 39, 40, 55, 58, 70, 90]
    i = 0
    j = 0
    n = len(a)

    while i < n and j < n:
        if a[i] < b[j]:
            i = i + 1
        elif b[j] < a[i]:
            j = j + 1
        else:
            print(a[i])
            i = i + 1
            j = j + 1


def unique_char_str():
    c = "aabc"
    hash_map = {}

    for char in c:
        if hash_map.get(char):
            print("Not unique")
            return
        else:
            hash_map[char] = True

    print("Unique")


def perm_palindram():
    s = "carerac"
    hash_map = {}
    for c in s:
        hash_map[c] = hash_map.get(c, 0) + 1

    flag = True
    for c in s:
        if len(s) % 2 != 0 and flag and hash_map.get(c) == 1:
            flag = False
        elif hash_map.get(c) % 2 != 0:
            return False
    return True


def one_edit():
    s1 = "pale"
    s2 = "plee"
    i, j = 0, 0
    m, n = len(s1), len(s2)
    if m > n:
        t = s1
        s1 = s2
        s2 = t
    is_one_edit = False
    while i < m and j < n:
        if s1[i] != s2[j]:
            if is_one_edit:
                return False
            if m == n:
                i += 1
                j += 1
            else:
                j += 1
            is_one_edit = True
        else:
            i += 1
            j += 1
    return True


def str_compression(s):
    n = len(s)
    res = []
    total_count = 0
    char_counter = 0
    i = 0
    j = 0
    while i < n and j < n:
        if s[i] == s[j]:
            char_counter = char_counter + 1
            j += 1
        else:
            total_count = total_count + 2
            res.append(s[i])
            res.append(str(char_counter))
            char_counter = 0
            i = j
        if j == n:
            res.append(s[i])
            res.append(str(char_counter))
            total_count = total_count + 2

    if total_count >= n:
        return s
    else:
        return "".join(res)


def rotate_matrix_90():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]
              ]
    n = len(matrix)
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            # swap
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            j = j + 1
        i = i + 1
    print(matrix)

    # reverse each row
    for i in range(n):
        matrix[i] = reverse_array(matrix[i])

    print(matrix)


def reverse_array(arr):
    n = len(arr)
    p = 0
    q = n - 1
    while p < q:
        t = arr[p]
        arr[p] = arr[q]
        arr[q] = t
        p += 1
        q -= 1
    return arr


def zero_matrix():
    matrix = [[1, 2, 3, 4],
              [5, 6, 0, 8],
              [10, 33, 5, 3]]
    m = len(matrix)
    n = len(matrix[0])
    rows_boo_ind = [False] * m
    column_bool_ind = [False] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_boo_ind[i] = True
                column_bool_ind[j] = True
    # for i in range(m):
    #     rows_boo_ind.append(check_zeros(matrix[i]))
    #
    # for i in range(n):
    #     is_zero = False
    #     for j in range(m):
    #         if matrix[j][i] == 0:
    #             is_zero = True
    #             break
    #     column_bool_ind.append(is_zero)

    print(rows_boo_ind)
    print(column_bool_ind)

    print(matrix)
    for i in range(m):
        for j in range(n):
            if rows_boo_ind[i] or column_bool_ind[j]:
                matrix[i][j] = 0

    print(matrix)


def check_zeros(arr):
    for each_ele in arr:
        if each_ele == 0:
            return True

    return False


def sub_array():
    n = 42
    s = 568
    arr = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183,
           22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
    # s = 12
    # n=5
    # arr = [1, 2, 3, 7, 5]
    run_sum = 0
    p = 0
    for q in range(n):
        while run_sum > s and p < q:
            run_sum = run_sum - arr[p]
            p = p + 1

        if run_sum == s:
            return [p+1,q]

        run_sum = run_sum + arr[q]

    # s = 12
    # n=5
    # arr = [1, 2, 3, 7, 5]
    # sum_matrix = [[0 for i in range(n)] for j in range(n)]
    #
    # for i in range(n):
    #     sum_matrix[i][i] = arr[i]
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         sum_matrix[i][j] = sum_matrix[i][j - 1] + arr[j]
    #
    # for i in range(n):
    #     for j in range(i, n):
    #         if sum_matrix[i][j] == s:
    #             return [i + 1, j + 1]


print(sub_array())
