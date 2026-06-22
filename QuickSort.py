def quickSort(a, low, high):
    if low < high:
        pivotIndex = getPivotIndex(a, low, high)

        quickSort(a, low, pivotIndex - 1)
        quickSort(a, pivotIndex + 1, high)


def getPivotIndex(a, low, high):
    pivot = a[high]

    i = low - 1
    j = low

    while j < high:
        if a[j] <= pivot:
            i += 1
            swap(a, i, j)

        j += 1

    swap(a, i + 1, high)

    return i + 1


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


nums = [1, 46, 3, 8, 5, 9, 3, 0, 4]

quickSort(nums, 0, len(nums) - 1)

print(nums)
    