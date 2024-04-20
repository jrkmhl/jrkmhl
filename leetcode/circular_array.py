def func():
    nums = [1, 2, 3, 4, 5, 6]
    n = len(nums)
    i = 3
    while i != 2:
        print(nums[i])
        i = (i + 1) % n

    # print(n)

func()
