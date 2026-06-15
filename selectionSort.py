'''*
Selection Sort is a comparison-based sorting algorithm. It sorts by repeatedly
selecting the smallest (or largest) element from the unsorted portion and swapping 
it with the first unsorted element.

Find the smallest element and swap it with the first element. 
This way we get the smallest element at its correct position.
Then find the smallest among remaining elements (or second smallest) and swap it 
with the second element.
We keep doing this until we get all elements moved to correct position.'''


def selectionSort(a):
    n=len(a)
    for i in range(n):
        min_element=a[i]
        min_index=i
        
        for j in range(i+1,n):
            if a[j]<min_element:
                min_element=a[j]
                min_index=j
                
        a[min_index]=a[i]
        a[i]=min_element
    return a
nums=[64,25,12,22,11]
print(selectionSort(nums))
    
    