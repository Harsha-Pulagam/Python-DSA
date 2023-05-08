def insertionsort(a):
    n = len(a)
    for i in range (1,n):
        x= a[i]                        # current element at index i is stored in the variable x.
        j=i-1                          # represents the index of the previous element.
        while j>=0 and x < a[j]:       # j >= 0 checks we haven't reached the beginning && current element is smaller than previous  
            a[j+1]=a[j]                # creates space for x to be inserted in the correct position
            j=j-1
        a[j+1] =x                      # inserted immediately after the element that is smaller than it.