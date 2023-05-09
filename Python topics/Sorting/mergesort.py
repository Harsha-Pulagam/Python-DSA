def merge_two_sorted_lists(a,b):
    'a,b are two sorted lists'
    res,i,j,m,n=[],0,0,len(a),len(b)
    while i<m and j<n:                      # loop continues until either i or j reaches the end of list a or b
        if a[i] > b[j]:
            res.append(b[j])
            j+=1
        else:
            res.append(a[i])
            i+=1
    #After above loop, there might be remaining elements that were not appended to res. To include those, two additional  loops are used:
    while i<m:
        res.append(a[i])                    # remaining elements of list a
        i+=1
    while j<n:
        res.append(b[j])                    # remaining elements of list b
        j+=1
    


def mergesort(a,low,mid,high):
    '''
    a -> list,low -> starting point of subarray, mid -> mid point of subarray, high ->ending point of subarray
    '''
    #auxilary lists
    left,right = a[low:mid+1],a[mid+1:high+1]
    i,j,k=0,0,low
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            a[k]=left[i]
            i+=1
            k+=1
        else:
            a[k]=right[j]
            j+=1
            k+=1
    while i<=len(left):
        a[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        a[k]=right[j]
        j+=1
        k+=1