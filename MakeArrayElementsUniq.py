def minIncrements( arr, N):
        mp = {i:0 for i in arr}
        print(mp)
        answer = 0
        for i in arr:
                if i in mp and mp[i] == 0:
                        mp[i] += 1
                elif i in mp:
                        temp = i
                        while temp in mp:
                                answer += 1
                                temp += 1
                        mp[temp] = 0
        return answer

minIncrements([1,2,3,4,4],5)
'''
Given an array arr[ ] of N elements, your task is to find the minimum number of increment operations required to make all the elements of the array unique. ie- no value in the array should occur more than once. 
In an operation a value can be incremented by 1 only.

Example 1:

Input:
N = 3
arr[] = {1, 2, 2}
Output:
1

Example :
Input: 
N = 4
arr[] = {1, 1, 2, 3}
Output:
3
Explanation: 
If we increase arr[0] by 3, then all array
elements will be unique. Hence, the answer 
is 3 in this case.
'''
'''
Intiuation
Step 1: First sort the array, A.
Step 2: Initialize an int variable, ans with 0.
Step 3: Now start iterating from second element till last.
Step 4: Let's say we are at ith position so if element at ith position is smaller or equal to (i-1)th then update A[i] with A[i-1]+1 as A[i] need to be unique and we can only increment. At this step add difference between new A[i] and old A[i] in ans.
Step 5: After iteration, return ans.
'''