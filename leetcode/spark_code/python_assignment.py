def find_duplicate(lst):
    """
    Timecomplexity - O(n)
    Space : O(n)
    """
    map = {}
    res = []
    for ele in lst:
        map[ele] = map.get(ele, 0) + 1

    unique_val = list(map.keys())

    for each_val in unique_val:
        if map.get(each_val) > 1:
            res.append(each_val)

    print("Duplicate elements :")
    print(res)
    return res


def find_duplicate2(lst) -> list:
    """
    Timecomplexity - O(n2)

    Space - O(1)
     Not including res as , we are using to just to store

    """
    res = set()
    n = len(lst)
    for i in range(n):
        for j in range(n):
            if i != j and lst[i] == lst[j]:
                res.add(lst[i])

    print("Duplicate elements :")
    print(list(res))
    return list(res)


def first_occurrence_dup(lst):
    """
    time compexity :O(n2)
    space complexity :O(n)
    """
    res = []
    temp = set()
    n = len(lst)
    for i in range(n):
        flag = False
        for j in range(n):
            if i != j and lst[i] == lst[j] and lst[i] not in temp:
                temp.add(lst[i])
                flag = True
                break
        if flag:
            # storing as tuple (element , index)
            res.append((lst[i], i))

    print("First occurrence of dup in (element, index) format :")
    print(res)


nums = [2, 5, 3, 4, 5, 7, 2, 2, 2, 2, 2, 11, 7, 9, 2, 3]
find_duplicate(nums)
find_duplicate2(nums)

first_occurrence_dup(nums)










