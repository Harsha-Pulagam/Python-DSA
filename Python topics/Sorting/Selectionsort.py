def Selectionsort(a):
    n = len(n)
    for i in range(n-1):  # iterates n - 1 times because the last element will automatically be in its correct position 
        min_index = i
        for j in range(i+1,n):# terates over the remaining unsorted elements of the list,
            if a[j] < a[min_index]:
                min_index=j
        a[min_index],a[i] = a[i],a[min_index]



