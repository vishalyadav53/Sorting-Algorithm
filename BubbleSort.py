'''Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping 
the adjacent elements if they are in the wrong order. This algorithm is not efficient 
for large data sets as its average and worst-case time complexity are quite high.

Sorts the array using multiple passes. After the first pass, the maximum goes to end
(its correct position).
Same way, after second pass, the second largest goes to second last position and so on.
In every pass, process only those that have already not moved to correct position.
After k passes, the largest k must have been moved to the last k positions.
In a pass, we consider remaining elements and compare all adjacent and swap if 
larger element is before a smaller element. If we keep doing this, we get the largest 
(among the remaining elements) at its correct position.'''
def BubbleSort(a):
    n = len(a)

    for i in range(0,n-1):    #i is for no of steps
        flag = True        #flag is used when the algorith if algorithm is already sorted

        for j in range(0,n-1-i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                flag = False

        if flag:          # loop will stop
            break

    return a

nums = [18,12,15,8,6]
print(BubbleSort(nums))