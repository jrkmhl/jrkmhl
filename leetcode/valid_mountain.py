def validMountainArray(arr: list[int]) -> bool:
    n = len(arr)
    if n < 3:
        return False

    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    print(j)
    j = n-1
    while j>=0 and arr[j-1]>arr[j]:
        j -=1

    print(j)

validMountainArray([0,2,3,4,5,2,1,0])