
def divide(a, low, high):
    if low < high:
        mid =low+(high-low) // 2
        divide(a, low, mid)
        divide(a, mid + 1, high)
        merge(a, low, mid, high)
        
        
def merge(a,low,mid,high):
    merged=[0]*(high-low+1)
    indx1,indx2,indx3=low,mid+1,0
    
    
    while indx1<=mid and indx2<=high:
        if a[indx1]<=a[indx2]:
            merged[indx3]=a[indx1]
            indx1+=1
            indx3+=1
        else:
            merged[indx3]=a[indx2]
            indx2+=1
            indx3+=1
            
        while indx1<=mid:
            merged[indx3]=a[indx1]
            indx1+=1
            indx3+=1
        while indx2<=high:
            merged[indx3]=a[indx2]
            indx2+=1
            indx3+=1
        i,j=low,0
        while i<low +len(merged):
            a[i]=merged[j]
            i+=1
            j+=1
a=[38,27,43,3,9,82,10]
print("before sorting",a)
divide(a,0,len(a)-1)
print("After sorting:",a)
            