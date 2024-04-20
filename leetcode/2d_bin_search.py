def searchMatrix(matrix, target: int) -> bool:
    m = len(matrix)
    i = 0
    j = m - 1

    while i <= j:

        mid_row = (i + j) // 2
        col0 = matrix[mid_row][0]
        coln = matrix[mid_row][-1]
        if col0 <= target <= coln:
            return bin_search(matrix[mid_row], target)
        elif target < col0:
            j = mid_row - 1
        elif target > coln:
            i = mid_row + 1

    return False


def bin_search(arr, target):
    print(arr)
    n = len(arr)
    i = 0
    j = n - 1

    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            j = mid - 1
        else:
            i = mid + 1

    return False


mat =[[1,3]]
ta = 3

searchMatrix(mat,3)