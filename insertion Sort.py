'''Insertion sort is a simple sorting algorithm that works by iteratively inserting each
element of an unsorted list into its correct position in a sorted portion of the list.
It is like sorting playing cards in your hands. 
You split the cards into two groups: the sorted cards and the unsorted cards.
Then, you pick a card from the unsorted group and put it in the right place in thesorted group.

Start with the second element as the first element is assumed to be sorted.
Compare the second element with the first if the second is smaller then swap them.
Move to the third element, compare it with the first two, and put it in its correct position
Repeat until the entire array is sorted.'''


def insertionSort(a):
    n=len(a)
    
    for i in range(1,n):
        pivot=a[i]
        j=i-1
        
        while j>=0 and a[j]>pivot:
            a[j+1]=a[j]
            j-=1
        a[j+1]=pivot
    return a
nums=[10,18,12,8,15,20,17]
print(insertionSort(nums))