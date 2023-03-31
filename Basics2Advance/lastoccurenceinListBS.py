#find the first occurance of element in a list
def findfirstocurrance(list,val):
    for i in range(0,len(list)):
        if list[i] == val:
            print(i)
            return 1
    return -1

#using BinarySearch find the last occurance of element in a list
def find_LastOcurranceBS(list,val):   #if list is not sorted sort it using sort()
    l,h=0,len(list)-1
    while l <= h:
        m = (l+h)//2
        if list[m] > val:
            h=m-1
        elif list[m] < val:
            l=m+1
        elif m == len(list) -1 or list[m] != list[m+1]:
            return m
        else:
            l = m+1
    return -1



list = [1,2,3,4,4,5,6,7,7,9]

findfirstocurrance(list,4)
find_LastOcurranceBS(list,7)