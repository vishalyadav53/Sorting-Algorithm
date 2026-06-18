'''Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows 
the Divide and Conquer approach. It works by recursively dividing the input array into two halves, recursively 
sorting the two halves and finally merging them back together to obtain the sorted array.'''



def MergeSort(a, b, c):
    indx1, indx2, indx3 = 0, 0, 0

    n1 = len(a)
    n2 = len(b)

    while indx1 < n1 and indx2 < n2:
        if a[indx1] <= b[indx2]:
            c[indx3] = a[indx1]
            indx1 += 1
        else:
            c[indx3] = b[indx2]
            indx2 += 1

        indx3 += 1

    while indx1 < n1:
        c[indx3] = a[indx1]
        indx1 += 1
        indx3 += 1

    while indx2 < n2:
        c[indx3] = b[indx2]
        indx2 += 1
        indx3 += 1

    return c


a = [20,22,25,26,28]
b = [12,14,16,18,20,23]

c = [0] * (len(a) + len(b))

print(MergeSort(a, b, c))