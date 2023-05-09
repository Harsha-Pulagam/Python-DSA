# 





# naive solution ->O(n^2)
def Bubblesort(a) -> list:
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]> a[j+1]:
                a[j], a[j+1] =  a[j+1],a[j]
    return a

#efficent


def Bubblesort(a) -> list:
    n=len(a)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if a[j]> a[j+1]:
                a[j], a[j+1] =  a[j+1],a[j]
                swapped = True
        if swapped == True:
            return a