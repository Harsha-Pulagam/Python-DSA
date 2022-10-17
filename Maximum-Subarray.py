'''
Questoin :
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]           Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]               Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]       Output: 23

Sol:
We can observe a lot of repeated calculations if we draw out the recursive tree for above solution -

                                                f(0, False)                       🔽 => repeated calculations
					                          /             \
                       		       f(1, False)              f(1, True)
			                      /          \             🔽          \           🔽
			                 f(2, False)      f(2, True)           f(2, True)
							/            \        🔽       \         🔽           \  🔽
						f(3, False)   f(3,True)     f(3, True)           f(3, True)
						/        \            \           \                  \                 \
				      ...        ...          ...         ...                ...               ...
These redundant calculations can be eliminated if we store the results for a given state and reuse them later whenever required rather than recalculating them over and over again.
Thus, we can use memoization technique here to make our solution more efficient. Here, we use a dp array where dp[mustPick][i] denotes the maximum sum subarray starting from i and mustPick denotes wheter the current element must be picked compulsorily or not.
'''
from functools import cache


class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i + 1, True), 0 if must_pick else solve(i + 1, False))

        return solve(0, False)
