# structure is used to return two values from minMax()
class pair:
    def __init__(self):
        self.min = 0
        self.max = 0


def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()

    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    # If there are more than one element, then initialize min and max
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax


if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)

    # Time Complexity: O(n)       Auxiliary Space: O(1)
'''
Further Ideas :
Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.
Time Complexity: O(n)  Auxiliary Space: O(log n)

By comparing them in pairs
Time Complexity: O(n)  Auxiliary Space: O(1)
'''