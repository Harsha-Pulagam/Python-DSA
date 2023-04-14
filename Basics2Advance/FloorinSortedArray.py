'''GFG 
Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing).

Example 1:
        Input:N = 7, x = 0 arr[] = {1,2,8,10,11,12,19} Output: -1
        Explanation: No element less than 0 is found. So output is "-1".
Example 2:
        Input: N = 7, x = 5 arr[] = {1,2,8,10,11,12,19} Output: 1
        Explanation: Largest Number less than 5 is 2 (i.e K = 2), whose index is 1(0-based indexing).'''

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        low = 0
        high = N-1
        while low <= high:
            mid = (low+high)//2
            if A[mid]==X:
                return mid
            if A[mid] > X :
                high = mid-1
            else:
                low = mid +1
        if A[high] < X:
            return high
        else:
            return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends